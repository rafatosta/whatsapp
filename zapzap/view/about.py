from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/templates/about.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Form.resize(420, 210)
        Form.setMinimumSize(QtCore.QSize(420, 210))
        Form.setMaximumSize(QtCore.QSize(420, 210))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.icon = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMinimumSize(QtCore.QSize(100, 100))
        self.icon.setMaximumSize(QtCore.QSize(100, 100))
        self.icon.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.icon.setScaledContents(False)
        self.icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.icon.setObjectName("icon")
        self.verticalLayout_2.addWidget(self.icon)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(15, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.version = QtWidgets.QLabel(Form)
        self.version.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.version.setObjectName("version")
        self.verticalLayout.addWidget(self.version)
        self.description_app = QtWidgets.QLabel(Form)
        self.description_app.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.description_app.setObjectName("description_app")
        self.verticalLayout.addWidget(self.description_app)
        self.developer = QtWidgets.QLabel(Form)
        self.developer.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.developer.setObjectName("developer")
        self.verticalLayout.addWidget(self.developer)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.license = QtWidgets.QLabel(Form)
        self.license.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.license.setObjectName("license")
        self.verticalLayout.addWidget(self.license)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        
        Form.setWindowTitle(_("About Zapzap"))
        self.icon.setText(_("icone do app"))
        self.name.setText(_("name"))
        self.version.setText(_("version"))
        self.description_app.setText(_("descrição"))
        self.developer.setText(_("Desenvolvedor"))
        self.license.setText(_("GNU General Public License v3.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
