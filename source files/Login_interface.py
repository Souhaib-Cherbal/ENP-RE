

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login_Dashboard(object):
    def setupUi(self, Login_Dashboard):
        Login_Dashboard.setObjectName("Login_Dashboard")
        Login_Dashboard.resize(400, 350)
        Login_Dashboard.setMinimumSize(QtCore.QSize(400, 350))
        Login_Dashboard.setMaximumSize(QtCore.QSize(400, 350))
        self.groupBox = QtWidgets.QGroupBox(Login_Dashboard)
        self.groupBox.setGeometry(QtCore.QRect(80, 90, 241, 181))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"  width: 320px;\n"
"  padding: 40px;\n"
"  background-color: #fff;\n"
"  border-radius: 5px;\n"
"  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(30, 40, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMouseTracking(True)
        self.username.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.username.setStyleSheet("QLineEdit{\n"
"  width: 100%;\n"
"  padding: 5px;\n"
"  border: 1px solid #ccc;\n"
"  border-radius: 3px;\n"
"  font-size: 12px;\n"
"}\n"
"QLineEdit:focus {\n"
"border-color: #66afe9;\n"
"outline : 0;\n"
"}")
        self.username.setClearButtonEnabled(False)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(30, 80, 181, 31))
        self.password.setStyleSheet("QLineEdit{\n"
"  width: 100%;\n"
"  padding: 5px;\n"
"  border: 1px solid #ccc;\n"
"  border-radius: 3px;\n"
"  font-size: 12px;\n"
"}\n"
"QLineEdit:focus {\n"
"border-color: #66afe9;\n"
"outline : 0;\n"
"}")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 130, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"  background-color: #213f98;\n"
"  color: #fff;\n"
"  padding:5 px 5px;\n"
"  border: none;\n"
"  border-radius: 3px;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #2980b9;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color : #213F98\n"
"\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Logo = QtWidgets.QLabel(Login_Dashboard)
        self.Logo.setGeometry(QtCore.QRect(140, 10, 131, 71))
        self.Logo.setStyleSheet("image: url(:/Logo-ENP.png);")
        self.Logo.setText("")
        self.Logo.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo.setObjectName("Logo")

        self.retranslateUi(Login_Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Login_Dashboard)
        self.Logo.setStyleSheet("image: url(Logo-ENP.png);")

    def retranslateUi(self, Login_Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Login_Dashboard.setWindowTitle(_translate("Login_Dashboard", "Réseau électrique ENP"))
        self.username.setPlaceholderText(_translate("Login_Dashboard", "Username"))
        self.password.setPlaceholderText(_translate("Login_Dashboard", "Password"))
        self.pushButton.setText(_translate("Login_Dashboard", "Log In"))
        self.label.setText(_translate("Login_Dashboard", "Login Dashboard"))

        self.setWindowFlags(
        self.windowFlags() | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint)