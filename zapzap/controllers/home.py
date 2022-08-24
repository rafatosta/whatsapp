import os
import shutil
from PyQt6.QtWidgets import QWidget
from zapzap.controllers.user_container import UserContainer
from zapzap.model.user import UserDAO
from zapzap.view.home import Ui_Home
import zapzap


class Home(QWidget, Ui_Home):
    """
    The Home Class manages the user bar and users' pages.
    The sidebar consists of custom qpushbutton and pages within a QSTackedwidget, 
    both with the same position.
    """
    list = None

    def __init__(self, parent=None):
        super(Home, self).__init__()
        self.setupUi(self)
        self.mainWindow = parent
        self.loadUsers()
        self.activeMenu()
        self.updateShortcuts()

    def loadUsers(self):
        """Carries all users from the database"""
        self.list = UserDAO.select()
        for user in self.list:
            button = UserContainer(self, user)
            self.menu.addWidget(button)
            self.userStacked.addWidget(button.getBrowser())

    def updateShortcuts(self):
        """Updates access shortcuts to users"""
        cont = 1
        for i in range(self.userStacked.count()):
            btn = self.menu.itemAt(i).widget()
            if btn.user.enable:
                btn.setShortcut(f'Ctrl+{cont}')
                cont += 1

    def addNewUser(self, user):
        """Add new user to the list, in the container (menu button) and the page at Stacked"""
        self.list.append(user)
        button = UserContainer(self, user)
        self.menu.addWidget(button)
        self.userStacked.addWidget(button.getBrowser())

        self.activeMenu()
        self.updateShortcuts()

    def activeMenu(self):
        """Activate the menu only for more than one user"""
        if len(self.list) > 1:
            self.menuUsers.show()
            self.menu.itemAt(0).widget().selected()
        else:
            self.menuUsers.hide()

    def resetStyle(self):
        """Restart the style of the user icons"""
        for i in reversed(range(self.menu.count())):
            ub = self.menu.itemAt(i).widget()
            ub.unselected()

    def setPage(self, browser):
        """Defines the page to be shown"""
        self.userStacked.setCurrentWidget(browser)

    def getUserContainer(self, idUser):
        """Take the container from the user ID"""
        for i in range(self.menu.count()):
            btn = self.menu.itemAt(i).widget()
            if btn.user.id == idUser:
                return btn, i
        return None

    def getSizeNotifications(self) -> int:
        """Sum the notifications of all users"""
        qtd = 0
        for i in range(self.menu.count()):
            btn = self.menu.itemAt(i).widget()
            qtd += btn.qtd
        return qtd

    def setThemePages(self, isNight_mode):
        """Define or theme for all pages page"""
        for i in range(self.menu.count()):
            btn = self.menu.itemAt(i).widget()
            btn.setThemePage(isNight_mode)

    def setZoomFactor(self, factor=None):
        """Current page zoom
            - Factor=None -> default (1.0).
            - factor:int -> Increases to the current value"""
        i = self.userStacked.currentIndex()
        btn = self.menu.itemAt(i).widget()
        btn.setZoomFactorPage(factor)

    def saveSettings(self):
        """Save settings all users"""
        for i in range(self.menu.count()):
            btn = self.menu.itemAt(i).widget()
            btn.saveSettings()

    def reloadPage(self):
        """Current page recharge"""
        i = self.userStacked.currentIndex()
        btn = self.menu.itemAt(i).widget()
        btn.doReloadPage()

    def setSpellChecker(self, lang):
        for i in range(self.menu.count()):
            btn = self.menu.itemAt(i).widget()
            btn.setSpellChecker(lang)

    def editUserPage(self, user):
        return_btn = self.getUserContainer(user.id)
        btn = return_btn[0]
        btn.setUser(user)

    def disableUserPage(self, user):
        """Disable user"""
        # If enabled, remove from stacked
        if user.enable:
            self.list.append(user)
            button = UserContainer(self, user)
            self.menu.addWidget(button)
            self.userStacked.addWidget(button.getBrowser())

            self.activeMenu()
            self.updateShortcuts()
        else:
            # Get UserContainer
            return_btn = self.getUserContainer(user.id)
            btn = return_btn[0]
            id_btn = return_btn[1]

            # Remove of userStacked
            self.userStacked.removeWidget(btn.getBrowser())

            # Remove icon of menu
            self.menu.itemAt(id_btn).widget().setParent(None)

            # Close browser
            btn.closeBrowser()

            # Update DB
            UserDAO.update(user)

            # Delete user list
            for u in self.list:
                if u.id == user.id:
                    self.list.remove(u)

            self.activeMenu()
            self.updateShortcuts()

    def delUserPage(self, user):
        """Delete user"""
        try:
            if user.enable:
                # Get UserContainer
                return_btn = self.getUserContainer(user.id)
                btn = return_btn[0]
                id_btn = return_btn[1]

                # Remove of userStacked
                self.userStacked.removeWidget(btn.browser)

                # Remove icon of menu
                self.menu.itemAt(id_btn).widget().setParent(None)

                # Close browser
                btn.closeBrowser()

            # Delete DB
            UserDAO.delete(user.id)

            # Delete user list
            for u in self.list:
                if u.id == user.id:
                    self.list.remove(u)

            # Delete User Data
            path = os.path.join(zapzap.path_storage, str(user.id))
            shutil.rmtree(path, ignore_errors=True)
        except OSError as error:
            print(error)
            print("File path can not be removed")
        else:
            print("% s removed successfully" % path)
        finally:
            self.activeMenu()
            self.updateShortcuts()

    def closeConversation(self):
        i = self.userStacked.currentIndex()
        btn = self.menu.itemAt(i).widget()
        btn.closeConversation()
    
