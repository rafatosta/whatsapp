from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl

import zapzap


class MenuBar():
    def __init__(self, mainWindow) -> None:
        # File
        mainWindow.actionSettings.triggered.connect(
            mainWindow.openSettings)
        mainWindow.actionDonations.triggered.connect(mainWindow.openDonations)
        mainWindow.actionQuit.triggered.connect(lambda x = None: mainWindow.closeEvent(x))
        mainWindow.actionClose_Conversation.triggered.connect(mainWindow.closeConversation)
        mainWindow.actionHide_on_close.triggered.connect(
            lambda: mainWindow.settings.setValue(
                "system/keep_background",  mainWindow.actionHide_on_close.isChecked()))

        # View
        mainWindow.actionReload_Service.triggered.connect(
            mainWindow.reload_Service)
        mainWindow.actionDefault_size_page.triggered.connect(
            mainWindow.setDefault_size_page)
        mainWindow.actionToggle_Full_Screen.triggered.connect(
            mainWindow.setFullSreen)
        mainWindow.actionZoomIn.triggered.connect(
            mainWindow.zoomIn)
        mainWindow.actionZoomOut.triggered.connect(
            mainWindow.zoomOut)
        mainWindow.actionAuto_hide_menu_bar.triggered.connect(
            mainWindow.setHideMenuBar)
        mainWindow.actionHome_page.triggered.connect(
            lambda: mainWindow.main_stacked.setCurrentIndex(0))

        # Help
        mainWindow.actionLearn_More.triggered.connect(lambda: QDesktopServices.openUrl(
            QUrl(zapzap.__website__)))
        mainWindow.actionChangelog.triggered.connect(lambda: QDesktopServices.openUrl(
            QUrl(zapzap.__releases__)))
        mainWindow.actionSupport.triggered.connect(lambda: QDesktopServices.openUrl(
            QUrl(zapzap.__bugreport__)))
        mainWindow.actionAbout_Zapzap.triggered.connect(
            mainWindow.openAbout_Zapzap)
