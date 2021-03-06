
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
from subprocess import call

class Ui_Dialog(object):

    def on_clicked1(self):
        call(["python","MainWindow.py"])

    def fileDailog(self):
        self.label_img.close()
        self.fileName = filedialog.askopenfilename(initialdir = "/", title="Select A File",filetype=(("jpeg","*.jpg"),("png","*.png")))
        root.destroy()
        path = self.fileName
        self.label_img = QtWidgets.QLabel(Dialog)
        self.label_img.setGeometry(QtCore.QRect(20, 150, 131, 121))
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap(path))
        self.label_img.setScaledContents(True)
        self.label_img.setObjectName("label_img")
        self.label_img.raise_()
        self.label_img.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(729, 499)
        self.label_BG = QtWidgets.QLabel(Dialog)
        self.label_BG.setGeometry(QtCore.QRect(-10, 0, 741, 501))
        self.label_BG.setText("")
        self.label_BG.setPixmap(QtGui.QPixmap("images/A.I2.png"))
        self.label_BG.setScaledContents(True)
        self.label_BG.setObjectName("label_BG")
        self.change_btn = QtWidgets.QPushButton(Dialog)
        self.change_btn.setGeometry(QtCore.QRect(370, 420, 141, 30))
        self.change_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.change_btn.setFont(font)
        self.change_btn.setObjectName("change_btn")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 150, 521, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_Uname = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Uname.setFont(font)
        self.label_Uname.setObjectName("label_Uname")
        self.gridLayout.addWidget(self.label_Uname, 0, 0, 1, 1)
        self.label_newpass = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_newpass.setFont(font)
        self.label_newpass.setObjectName("label_newpass")
        self.gridLayout.addWidget(self.label_newpass, 2, 0, 1, 1)
        self.label_prepass = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_prepass.setFont(font)
        self.label_prepass.setObjectName("label_prepass")
        self.gridLayout.addWidget(self.label_prepass, 1, 0, 1, 1)
        self.le_newpass = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_newpass.setFont(font)
        self.le_newpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_newpass.setObjectName("le_newpass")
        self.gridLayout.addWidget(self.le_newpass, 2, 1, 1, 1)
        self.le_PrePass = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_PrePass.setFont(font)
        self.le_PrePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_PrePass.setObjectName("le_PrePass")
        self.gridLayout.addWidget(self.le_PrePass, 1, 1, 1, 1)
        self.le_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_name.setFont(font)
        self.le_name.setObjectName("le_name")
        self.gridLayout.addWidget(self.le_name, 0, 1, 1, 1)
        self.label_newpass_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_newpass_2.setFont(font)
        self.label_newpass_2.setObjectName("label_newpass_2")
        self.gridLayout.addWidget(self.label_newpass_2, 3, 0, 1, 1)
        self.le_Cnewpass = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_Cnewpass.setFont(font)
        self.le_Cnewpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_Cnewpass.setObjectName("le_Cnewpass")
        self.gridLayout.addWidget(self.le_Cnewpass, 3, 1, 1, 1)
        self.label_Logo = QtWidgets.QLabel(Dialog)
        self.label_Logo.setGeometry(QtCore.QRect(0, 0, 111, 101))
        self.label_Logo.setText("")
        self.label_Logo.setPixmap(QtGui.QPixmap("images/Logo.png"))
        self.label_Logo.setScaledContents(True)
        self.label_Logo.setObjectName("label_Logo")
        self.label_Title = QtWidgets.QLabel(Dialog)
        self.label_Title.setGeometry(QtCore.QRect(110, 10, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_Title.setFont(font)
        self.label_Title.setObjectName("label_Title")
        self.label_setting = QtWidgets.QLabel(Dialog)
        self.label_setting.setGeometry(QtCore.QRect(360, 90, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_setting.setFont(font)
        self.label_setting.setObjectName("label_setting")
        self.label_admin = QtWidgets.QLabel(Dialog)
        self.label_admin.setGeometry(QtCore.QRect(20, 280, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_admin.setFont(font)
        self.label_admin.setObjectName("label_admin")
        self.label_img = QtWidgets.QLabel(Dialog)
        self.label_img.setGeometry(QtCore.QRect(20, 150, 131, 121))
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap("images/Logo.png"))
        self.label_img.setScaledContents(True)
        self.label_img.setObjectName("label_img")
        self.back_btn = QtWidgets.QPushButton(Dialog)
        self.back_btn.setGeometry(QtCore.QRect(644, 30, 71, 25))
        self.back_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.back_btn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(30, 30))
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(Dialog.close)
        self.back_btn.clicked.connect(self.on_clicked1)
        self.upload_btn = QtWidgets.QToolButton(Dialog)
        self.upload_btn.setGeometry(QtCore.QRect(140, 260, 30, 25))
        self.upload_btn.setMaximumSize(QtCore.QSize(30, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/addimg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_btn.setIcon(icon1)
        self.upload_btn.setIconSize(QtCore.QSize(30, 30))
        self.upload_btn.setObjectName("toolButton")
        self.upload_btn.clicked.connect(self.fileDailog)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.change_btn.setText(_translate("Dialog", "Change"))
        self.label_Uname.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Change User Name</span></p></body></html>"))
        self.label_newpass.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Enter New Password</span></p></body></html>"))
        self.label_prepass.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Enter Previous Password</span></p></body></html>"))
        self.label_newpass_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Confirm New Password</span></p></body></html>"))
        self.label_Title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Smart Security System</span></p></body></html>"))
        self.label_setting.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#000000;\">Settings</span></p></body></html>"))
        self.label_admin.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Admin</span></p></body></html>"))
        self.back_btn.setText(_translate("Dialog", "Back"))




if __name__ == "__main__":
    import sys
    root = tk.Tk()
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
