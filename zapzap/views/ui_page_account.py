from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/ui/ui_page_account.ui'
#
# Created by: PyQt6 UI code generator 6.8.1.dev2502011625
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PageAccount(object):
    def setupUi(self, PageAccount):
        PageAccount.setObjectName("PageAccount")
        PageAccount.resize(693, 620)
        PageAccount.setWindowTitle("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(PageAccount)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(parent=PageAccount)
        self.frame.setMinimumSize(QtCore.QSize(550, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.btn_new_user = QtWidgets.QPushButton(parent=self.frame)
        self.btn_new_user.setObjectName("btn_new_user")
        self.verticalLayout_2.addWidget(self.btn_new_user)
        self.frame_accounts = QtWidgets.QFrame(parent=self.frame)
        self.frame_accounts.setStyleSheet("")
        self.frame_accounts.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_accounts.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_accounts.setObjectName("frame_accounts")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_accounts)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.user_list_layout = QtWidgets.QVBoxLayout()
        self.user_list_layout.setContentsMargins(0, 0, 0, 0)
        self.user_list_layout.setObjectName("user_list_layout")
        self.verticalLayout_4.addLayout(self.user_list_layout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 189, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame_accounts)
        self.horizontalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 295, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)

        self.retranslateUi(PageAccount)
        QtCore.QMetaObject.connectSlotsByName(PageAccount)

    def retranslateUi(self, PageAccount):
        
        self.label.setText(_("My accounts"))
        self.btn_new_user.setText(_("New account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PageAccount = QtWidgets.QWidget()
    ui = Ui_PageAccount()
    ui.setupUi(PageAccount)
    PageAccount.show()
    sys.exit(app.exec())
