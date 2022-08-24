from PyQt6.QtWidgets import QMainWindow, QSystemTrayIcon
from PyQt6.QtCore import QSettings, QByteArray, QTimer
from zapzap.theme.zap_themes import getThemeDark, getThemeLight
from zapzap.controllers.main_window_components.menu_bar import MenuBar
from zapzap.controllers.main_window_components.tray_icon import TrayIcon
from zapzap.controllers.main_window_decoration.ui_decoration import UIDecoration
from zapzap.controllers.settings import Settings
from zapzap.controllers.home import Home
from zapzap.services.dbus_theme import get_system_theme
import zapzap
from gettext import gettext as _

from zapzap.view.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    isFullScreen = False
    isHideMenuBar = False

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.app = parent
        self.settings = QSettings(zapzap.__appname__, zapzap.__appname__)
        self.scd = None

        # Object responsible for managing the main window menu bar
        MenuBar(self)

        # Object responsible for managing the tray icon
        self.tray = TrayIcon(self)

        # create pages
        self.zapHome = Home(self)
        self.zapSettings = Settings(self)
        self.zapSettings.updateUsersShortcuts()

        # Insert pages in main window
        self.main_stacked.insertWidget(0, self.zapHome)
        self.main_stacked.insertWidget(1, self.zapSettings)

        # timer for system theme change check (check in 1s)
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.current_theme = -1

        self.setZapDecoration()

    def emitSetSpellChecker(self, lang):
        self.zapHome.setSpellChecker(lang)

    def emitNewUser(self, user):
        """Function called by the setting panel when ADDING new user."""
        self.zapHome.addNewUser(user)
        self.zapSettings.updateUsersShortcuts()

    def emitDeleteUser(self, user):
        """Function called by the setting panel when DELETE user."""
        self.zapHome.delUserPage(user)
        self.zapSettings.updateUsersShortcuts()

    def emitDisableUser(self, user):
        """Function called by the setting panel when DISABLE/ENABLE user. """
        self.zapHome.disableUserPage(user)
        self.zapSettings.updateUsersShortcuts()

    def emitEditUser(self, user):
        """Function called by the setting panel when EDIT user. """
        self.zapHome.editUserPage(user)

    def emitNotifications(self):
        """The notifications of all users to the tray"""
        qtd = self.zapHome.getSizeNotifications()

        if qtd > 0:
            self.setWindowTitle(zapzap.__appname__+" ("+str(qtd)+")")
        else:
            self.setWindowTitle(zapzap.__appname__)

        self.tray.showIconNotification(qtd)

    def setZapDecoration(self):
        """Activate the personalized window"""
        self.headbar.hide()
        if self.settings.value("system/zap_decoration", True, bool):
            self.scd = UIDecoration(self)

    def recurring_timer(self):
        """ Check the current system theme and apply it in the app """
        theme = get_system_theme()
        if self.current_theme != theme:
            self.current_theme = theme
            self.setThemeApp(self.current_theme)

    def setThemeApp(self, isNight_mode):
        """"Apply the theme in the APP
            isNight_mode: boll
        """
        if isNight_mode:
            self.app.setStyleSheet(getThemeDark())
        else:
            self.app.setStyleSheet(getThemeLight())

        # Apply equivalent theme on whatsapp page
        self.zapHome.setThemePages(isNight_mode)

    def reload_Service(self):
        """Refreshing the page"""
        self.zapHome.reloadPage()

    def openTraySettings(self):
        """Opens the settings from the tray"""
        if self.app.activeWindow() == None:  # Se a janela estiver em foco será escondida
            self.show()
            self.app.activateWindow()

        self.main_stacked.setCurrentIndex(1)

    def openSettings(self):
        """Open settings"""
        if self.main_stacked.currentIndex() == 1:
            self.main_stacked.setCurrentIndex(0)
        else:
            self.main_stacked.setCurrentIndex(1)
            self.zapSettings.goPageHome()

    def openDonations(self):
        """Open settings"""
        self.main_stacked.setCurrentIndex(1)
        self.zapSettings.goPageDonations()

    def openAbout_Zapzap(self):
        """Open About"""
        self.main_stacked.setCurrentIndex(1)
        self.zapSettings.goPageHelp()

    def loadSettings(self):
        """
        Load the settings
        """
        # Theme App
        theme_mode = self.settings.value("system/theme", 'auto', str)
        if theme_mode == 'auto':
            self.setThemeApp(get_system_theme())
            self.timer.start()
        elif theme_mode == 'light':
            self.setThemeApp(False)
        else:
            self.setThemeApp(True)
        # MenuBar
        self.isHideMenuBar = self.settings.value(
            "main/hideMenuBar", False, bool)
        self.setHideMenuBar()
        # keep_background
        self.actionHide_on_close.setChecked(self.settings.value(
            "system/keep_background", True, bool))
        # Window State
        self.restoreGeometry(self.settings.value(
            "main/geometry", QByteArray()))
        self.restoreState(self.settings.value(
            "main/windowState", QByteArray()))

    def saveSettings(self):
        """Save Settings"""
        self.settings.setValue("main/geometry", self.saveGeometry())
        self.settings.setValue("main/windowState", self.saveState())
        # Warns the Home so that users save their settings
        self.zapHome.saveSettings()

    def closeEvent(self, event):
        """
            Override the window close event.
            Save window dimensions and check if it should be hidden or closed
        """
        self.timer.stop()
        isBack = self.settings.value("system/keep_background", True, bool)
        if isBack and event:  # Hide app on close window
            self.hide()
            event.ignore()
        else:  # Quit app on close window
            self.saveSettings()
            self.hide()
            self.app.quit()

    def onTrayIconActivated(self, reason):
        """
        wind to show and hide the window with just two click or middle button on the tray icon. 
        One click opens the menu.
        """
        if reason == QSystemTrayIcon.ActivationReason.Trigger or reason == QSystemTrayIcon.ActivationReason.MiddleClick:
            self.on_show()
            self.app.activateWindow()

    def on_show(self):
        """
        Opening the system tray web app.
        """
        if self.app.activeWindow() != None:  # Se a janela estiver em foco será escondida
            self.hide()
        else:  # Caso não esteja, será mostrada
            self.hide()
            self.show()
            self.app.activateWindow()
            self.main_stacked.setCurrentIndex(0)

    def setDefault_size_page(self):
        """Reset user defined zoom (1.0 by default)"""
        self.zapHome.setZoomFactor()

    def zoomIn(self):
        """Zoom in"""
        self.zapHome.setZoomFactor(+0.1)

    def zoomOut(self):
        """zoom out"""
        self.zapHome.setZoomFactor(-0.1)

    def setFullSreen(self):
        """
        Full Screen Window
        """
        if not self.isFullScreen:
            self.showFullScreen()
        else:
            self.showNormal()
        self.isFullScreen = not self.isFullScreen

    def setHideMenuBar(self):
        """Hides/Shows the menu bar in the system window"""
        if self.settings.value("system/zap_decoration", True, bool):
            self.menubar.setMaximumHeight(0)
        else:
            """
            Hide/Show MenuBar
            """
            if self.isHideMenuBar:
                self.menubar.setMaximumHeight(0)
            else:
                # default size for qt designer
                self.menubar.setMaximumHeight(16777215)

            self.settings.setValue("main/hideMenuBar", self.isHideMenuBar)
            self.zapSettings.menubar.setChecked(self.isHideMenuBar)
            self.isHideMenuBar = not self.isHideMenuBar
    
    def closeConversation(self):
        """"Closes the current conversation, if any"""
        self.zapHome.closeConversation()
