from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/card_user.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CardUser(object):
    def setupUi(self, CardUser):
        CardUser.setObjectName("CardUser")
        CardUser.resize(620, 92)
        CardUser.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(CardUser)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=CardUser)
        self.frame.setMinimumSize(QtCore.QSize(620, 0))
        self.frame.setMaximumSize(QtCore.QSize(620, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.icon = QtWidgets.QLabel(parent=self.frame)
        self.icon.setMinimumSize(QtCore.QSize(64, 64))
        self.icon.setMaximumSize(QtCore.QSize(64, 64))
        self.icon.setText("")
        self.icon.setScaledContents(True)
        self.icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.icon.setObjectName("icon")
        self.horizontalLayout_3.addWidget(self.icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QLineEdit(parent=self.frame)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.btnDisable = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDisable.sizePolicy().hasHeightForWidth())
        self.btnDisable.setSizePolicy(sizePolicy)
        self.btnDisable.setMinimumSize(QtCore.QSize(100, 30))
        self.btnDisable.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnDisable.setObjectName("btnDisable")
        self.horizontalLayout.addWidget(self.btnDisable)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.key = QtWidgets.QLabel(parent=self.frame)
        self.key.setText("")
        self.key.setObjectName("key")
        self.horizontalLayout_2.addWidget(self.key)
        self.btnDelete = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        self.btnDelete.setMinimumSize(QtCore.QSize(100, 30))
        self.btnDelete.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout_2.addWidget(self.btnDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(CardUser)
        QtCore.QMetaObject.connectSlotsByName(CardUser)

    def retranslateUi(self, CardUser):
        
        CardUser.setWindowTitle(_("Form"))
        self.name.setPlaceholderText(_("Enter the user name"))
        self.btnDisable.setText(_("Disable"))
        self.btnDelete.setText(_("Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CardUser = QtWidgets.QWidget()
    ui = Ui_CardUser()
    ui.setupUi(CardUser)
    CardUser.show()
    sys.exit(app.exec())
