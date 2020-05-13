# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'google_login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(405, 516)
        Form.setStyleSheet("#Form{\n"
"background-color:white;\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(120, -10, 161, 71))
        self.frame.setStyleSheet("QFrame{\n"
"background-color:transparent;\n"
"border:none;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(20, 20, 120, 40))
        self.frame_5.setStyleSheet("border-image: url(:/newPrefix/googlelogo_color_160x56dp.png);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(80, 70, 280, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("QLabel{\n"
"color:#898989;\n"
"}")
        self.label_1.setObjectName("label_1")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 120, 560, 450))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color:#F7F7F7;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"border:none;\n"
"border-bottom:1px solid rgba(0,0,0,.3);\n"
"border-right:1px solid rgba(0,0,0,.3);\n"
"border-left: 1px solid rgba(0,0,0,.3);\n"
"border-top: 1px solid rgba(0,0,0,.3);\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:1px solid #4C8AF9;\n"
"border-right:1px solid #4C8AF9;\n"
"border-left: 1px solid  #4C8AF9;\n"
"border-top: 1px solid #4C8AF9;\n"
"\n"
"\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(150, 0, 140, 110))
        self.frame_3.setStyleSheet("QFrame{\n"
"background-color:transparent;\n"
"border:none;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 10, 90, 80))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/download.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.Email_lineedit = QtWidgets.QLineEdit(self.frame_2)
        self.Email_lineedit.setGeometry(QtCore.QRect(90, 120, 230, 40))
        self.Email_lineedit.setStyleSheet("")
        self.Email_lineedit.setObjectName("Email_lineedit")
        self.password_lineedit = QtWidgets.QLineEdit(self.frame_2)
        self.password_lineedit.setGeometry(QtCore.QRect(90, 165, 230, 40))
        self.password_lineedit.setObjectName("password_lineedit")
        self.signin_button = QtWidgets.QPushButton(self.frame_2)
        self.signin_button.setGeometry(QtCore.QRect(70, 240, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signin_button.setFont(font)
        self.signin_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signin_button.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"background-color:#4C8AF9;\n"
"color:white;\n"
"\n"
"}")
        self.signin_button.setObjectName("signin_button")
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setGeometry(QtCore.QRect(80, 290, 110, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(310, 370, 80, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet("QLabel{\n"
"color:#4C8AF9;\n"
"\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:black;\n"
"text-decoration: overline;\n"
"\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_1.setText(_translate("Form", "Sign in with your Google Account"))
        self.signin_button.setText(_translate("Form", "Sign in"))
        self.checkBox.setText(_translate("Form", "Stay signed in"))
        self.label_2.setText(_translate("Form", "Need help ?"))
import img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
