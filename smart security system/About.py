# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(539, 382)
        self.BG_label = QtWidgets.QLabel(About)
        self.BG_label.setGeometry(QtCore.QRect(0, -8, 621, 451))
        self.BG_label.setText("")
        self.BG_label.setPixmap(QtGui.QPixmap("images/BG3.jpeg"))
        self.BG_label.setScaledContents(True)
        self.BG_label.setObjectName("BG_label")
        self.label_Logo = QtWidgets.QLabel(About)
        self.label_Logo.setGeometry(QtCore.QRect(0, 0, 111, 101))
        self.label_Logo.setText("")
        self.label_Logo.setPixmap(QtGui.QPixmap("images/Logo.png"))
        self.label_Logo.setScaledContents(True)
        self.label_Logo.setObjectName("label_Logo")
        self.label_Title = QtWidgets.QLabel(About)
        self.label_Title.setGeometry(QtCore.QRect(110, 10, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_Title.setFont(font)
        self.label_Title.setObjectName("label_Title")
        self.abt_textEdit = QtWidgets.QTextEdit(About)
        self.abt_textEdit.setGeometry(QtCore.QRect(50, 100, 441, 251))
        self.abt_textEdit.setStyleSheet("background-color: rgb(6, 37, 58);")
        self.abt_textEdit.setObjectName("abt_textEdit")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Dialog"))
        self.label_Title.setText(_translate("About", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Smart Security System</span></p></body></html>"))
        self.abt_textEdit.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#ffffff;\">About</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-size:10pt; color:#ffffff;\">Our system is an &quot;A.I Based Smart Security by Face Recognition&quot;. It helps Organizations, Institute or any Company to make there environment secure. We use modern technologies like, Face APi\'s, Mobile Net SSD etc. to make sure that it will provise the best. There would be multi-face detected by camera which is connect to a system. The system will recognize multi-faces and shows that the recognized face must be an Employees, Visitors or Unwanted persons. The entire process is triggered by a camera, which is installed on a device that’s connected to a camera. The system detects faces, persons and vehicles in the stream and notify the authorities if any unknow person tries to enter in the premises. </span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())