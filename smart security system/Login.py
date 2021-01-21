import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from subprocess import call
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_Login_Form(object):

    def pop_window(self, text):

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        msg.setWindowTitle("{}".format(text))
        msg.exec_()


    def on_click(self):

        if ((len(self.password.text())) and (len(self.user_name.text()))) < 1:
            Login_Form.show()
            self.pop_window('Both Fields Are Required !')

        elif ((len(self.password.text()) <= 2)) and ((len(self.user_name.text()) <= 2)):
            Login_Form.show()
            self.pop_window('Invalid User or Password !')

        elif ((len(self.password.text()) <= 5)) and ((len(self.user_name.text()) > 2)):
            Login_Form.show()
            self.pop_window('Password Should Be Above 5 Character !')


        else:
            username = self.user_name.text()
            password = self.password.text()

            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Arbaz123", database="mydb")
            conn = mydb.cursor()
            query = """SELECT COUNT(*) FROM SystemUser  WHERE User_Name = %s AND Password = %s"""
            value =  ( username, password )
            conn.execute(query,value)
            val = conn.fetchone()

            if val[0] == 1:

              call(["python", "MainWindow.py"])

            else:
                Login_Form.show()
                self.pop_window('No User Found With This Password !')

###################################################################################################

    def reset(self):
        call(["python","ResetDia.py"])




#########################################################################################################

    def close(self):
        msg = QMessageBox()
        msg.setWindowTitle("Are You Sure")
        msg.setText("Do You Want To Quit")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(self.afterclose)
        x = msg.exec_()

    def afterclose(self, i):
        if len(i.text()) <= 3:
            #print(len(i.text()))
            Login_Form.show()
        else:
            exit()

################################################################################################

    def setupUi(self, Login_Form):
        Login_Form.setObjectName("Login_Form")
        Login_Form.resize(797, 397)
        Login_Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Login_Form.setAutoFillBackground(True)
        Login_Form.setStyleSheet("")
        self.Title = QtWidgets.QLabel(Login_Form)
        self.Title.setGeometry(QtCore.QRect(40, 30, 731, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAutoFillBackground(False)
        self.Title.setStyleSheet("background-image: url(:/newPrefix/images/A.I2);""\n""\n""color: white;\n""border-syle: outset;\n""border-width: 2px;\n""border-color:black;\n""font: bold 14px;\n""font-size:40px;\n""\n""")
        self.Title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Title.setLineWidth(1)
        self.Title.setTextFormat(QtCore.Qt.RichText)
        self.Title.setScaledContents(False)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.label_pass = QtWidgets.QLabel(Login_Form)
        self.label_pass.setGeometry(QtCore.QRect(230, 200, 100, 30))
        self.label_pass.setMinimumSize(QtCore.QSize(100, 30))
        self.label_pass.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_pass.setFont(font)
        self.label_pass.setMouseTracking(True)
        # self.label_pass.setStyleSheet("background-color: rgb(0, 0, 0);\n""\n""color: black;\n""border-syle: outset;\n""border-width: 2px;\n""border-color:black;\n""font: bold 14px;\n""font-size:18px;\n""\n""")
        #self.label_pass.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.label_pass.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pass.setObjectName("label_pass")
        self.password = QtWidgets.QLineEdit(Login_Form)
        self.password.setGeometry(QtCore.QRect(340, 200, 200, 30))
        self.password.setMinimumSize(QtCore.QSize(200, 30))
        self.password.setMaximumSize(QtCore.QSize(250, 30))
        self.password.setStyleSheet("QLineEdit{ \n""background-color: rgb(255, 255, 255);\n" "}")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setStyleSheet("font: 14px")
        self.password.setPlaceholderText("Type Your Password")
        self.password.setObjectName("password")
        self.label_Uname = QtWidgets.QLabel(Login_Form)
        self.label_Uname.setGeometry(QtCore.QRect(230, 130, 100, 30))
        self.label_Uname.setMinimumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_Uname.setFont(font)
       # self.label_Uname.setStyleSheet("selection-color: rgb(255, 255, 255);\n""\n""color: white;\n""font: bold 14px;\n""font-size:18px;\n""\n""")
        #self.label_Uname.setFrameShape(QtWidgets.QFrame.StyledPanel)
      #  self.label_Uname.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_Uname.setTextFormat(QtCore.Qt.RichText)
        self.label_Uname.setScaledContents(False)
        self.label_Uname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Uname.setObjectName("label_Uname")
        self.user_name = QtWidgets.QLineEdit(Login_Form)
        self.user_name.setGeometry(QtCore.QRect(340, 130, 200, 30))
        self.user_name.setMinimumSize(QtCore.QSize(200, 30))
        self.user_name.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.user_name.setFont(font)
        self.user_name.setAutoFillBackground(False)
        self.user_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.user_name.setStyleSheet("font: 14px")
        self.user_name.setPlaceholderText("Type User_ID Here")
        self.user_name.setObjectName("user_name")
        self.BG_label = QtWidgets.QLabel(Login_Form)
        self.BG_label.setGeometry(QtCore.QRect(0, 0, 811, 411))
        self.BG_label.setStyleSheet("")
        self.BG_label.setText("")
        self.BG_label.setPixmap(QtGui.QPixmap("images/A.I2.PNG"))
        self.BG_label.setScaledContents(True)
        self.BG_label.setObjectName("BG_label")
        self.close_btn = QtWidgets.QPushButton(Login_Form)
        self.close_btn.setGeometry(QtCore.QRect(610, 320, 140, 40))
        self.close_btn.setStyleSheet("background-color: rgb(0, 170, 255);\n""\n""color: white;\n""border-syle: outset;\n""border-width: 2px;\n""border-color:black;\n""font: bold 10px;\n""font-size:14px;\n""\n""")
        self.close_btn.setObjectName("close_btn")
        self.close_btn.clicked.connect(self.close)
        self.reset_btn = QtWidgets.QPushButton(Login_Form)
        self.reset_btn.setGeometry(QtCore.QRect(30, 320, 140, 40))
        self.reset_btn.setStyleSheet("background-color: rgb(0, 170, 255);\n""\n""color: white;\n""border-syle: outset;\n""border-width: 2px;\n""border-color:black;\n""font: bold 10px;\n""font-size:14px;\n""\n""")
        self.reset_btn.setObjectName("reset_btn")
        self.reset_btn.clicked.connect(self.reset)
        self.login_btn = QtWidgets.QPushButton(Login_Form)
        self.login_btn.setGeometry(QtCore.QRect(320, 260, 140, 40))
        self.login_btn.setStyleSheet("background-color: rgb(0, 170, 255);\n""\n""color: black;\n""border-syle: outset;\n""border-width: 2px;\n""border-color:black;\n""font: bold 10px;\n""font-size:14px;\n""\n""background-color: rgb(0, 255, 255);")
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(Login_Form.close)
        self.login_btn.clicked.connect(self.on_click)
        self.BG_label.raise_()
        self.label_Uname.raise_()
        self.Title.raise_()
        self.label_pass.raise_()
        self.password.raise_()
        self.user_name.raise_()
        self.close_btn.raise_()
        self.login_btn.raise_()
        self.reset_btn.raise_()
        self.retranslateUi(Login_Form)
        QtCore.QMetaObject.connectSlotsByName(Login_Form)

    def retranslateUi(self, Login_Form):
        _translate = QtCore.QCoreApplication.translate
        Login_Form.setWindowTitle(_translate("Login_Form", "Smart Securit System"))
        self.Title.setText(_translate("Login_Form", "Welcome To Smart Security System"))
        self.label_pass.setText(_translate("Login_Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Password</span></p></body></html>"))
        #self.password.setToolTip(_translate("Login_Form", "<html><head/><body><p>Enter password here</p></body></html>"))
        self.label_Uname.setText(_translate("Login_Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">User Name</span></p></body></html>"))
        #self.user_name.setToolTip(_translate("Login_Form", "<html><head/><body><p>Enter user name here</p></body></html>"))
        self.close_btn.setToolTip(_translate("Login_Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:50; color:black;\">It Will Close The System</span></p></body></html>"))
        self.close_btn.setText(_translate("Login_Form", "Close System"))
        self.reset_btn.setToolTip(_translate("Login_Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:50; color:black;\">It Will Reset System Password </p></body></html>"))
        self.reset_btn.setText(_translate("Login_Form", "Reset Password"))
        self.login_btn.setToolTip(_translate("Login_Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:100; color:black;\">It Will Login Into The System<span></p></body></html>"))
        self.login_btn.setText(_translate("Login_Form", "Login "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Form = QtWidgets.QWidget()
    ui = Ui_Login_Form()
    ui.setupUi(Login_Form)
    Login_Form.show()
    sys.exit(app.exec_())