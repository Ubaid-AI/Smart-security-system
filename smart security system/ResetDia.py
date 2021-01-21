import  mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Arbaz123", database="mydb")

class Ui_Dialog(object):

    def pop_window(self, text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        msg.setWindowTitle("{}".format(text))
        msg.exec_()

    def pop_window2(self, text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("{}".format(text))
        msg.setWindowTitle("{}".format(text))
        msg.exec_()

    def after_reset(self):

        if ((len(self.le_name.text()) < 1)) or ((len(self.le_prepass.text()) < 1 )) or ((len(self.le_newpass.text()) < 1)) or ((len(self.le_Cnewpass.text()) < 1)):
            self.pop_window('All Fields Are Required')


        elif ((len(self.le_name.text()) <= 2)):
            self.pop_window(' Invalid Username ')

        elif ((len(self.le_name.text()) > 2)) and ((len(self.le_prepass.text()) <= 5)) and ((len(self.le_newpass.text()) <= 5)) and ((len(self.le_Cnewpass.text()) <= 5)):
            self.pop_window(' Password Must Be Greator Than 5 Character')

        else:
            username = self.le_name.text()
            password = self.le_prepass.text()
            newpass = self.le_newpass.text()
            cpassword = self.le_Cnewpass.text()

            if ((newpass != cpassword)):
                self.pop_window(' Make Sure That Password Must Be Correct ')

            else:
                mydb = mysql.connector.connect(host="localhost", user="root", passwd="Arbaz123", database="mydb")
                conn = mydb.cursor()
                conn.execute("SELECT User_Name,Password FROM SystemUser")
                val = conn.fetchall()

                if len(val) >= 1:

                    for x in val:

                        if ((username in x[0]) and (password in x[1])):

                         num = "1"
                         mydb = mysql.connector.connect(host="localhost", user="root", passwd="Arbaz123",database="mydb")
                         con = mydb.cursor()
                         querry = """UPDATE SystemUser SET Password = %s WHERE Id = %s"""
                         value = (newpass, num)
                         con.execute(querry, value)
                         mydb.commit()
                         self.pop_window2("Password Has Changed Successfully.")

                         break


                        else:
                            self.pop_window('No User Found With This Password !')
                            break

                else:
                    self.pop_window('No user Found')



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(277, 389)
        self.label_BG = QtWidgets.QLabel(Dialog)
        self.label_BG.setGeometry(QtCore.QRect(-4, 0, 281, 391))
        self.label_BG.setText("")
        self.label_BG.setPixmap(QtGui.QPixmap("images/A.I2.PNG"))
        self.label_BG.setScaledContents(True)
        self.label_BG.setObjectName("label_BG")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 201, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Uname = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Uname.setFont(font)
        self.label_Uname.setObjectName("label_Uname")
        self.verticalLayout.addWidget(self.label_Uname)
        self.le_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_name.setFont(font)
        self.le_name.setObjectName("le_name")
        self.verticalLayout.addWidget(self.le_name)
        self.label_prepass = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_prepass.setFont(font)
        self.label_prepass.setObjectName("label_prepass")
        self.verticalLayout.addWidget(self.label_prepass)
        self.le_prepass = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_prepass.setFont(font)
        self.le_prepass.setObjectName("le_prepass")
        self.verticalLayout.addWidget(self.le_prepass)
        self.label_newpass = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_newpass.setFont(font)
        self.label_newpass.setObjectName("label_newpass")
        self.verticalLayout.addWidget(self.label_newpass)
        self.le_newpass = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_newpass.setFont(font)
        self.le_newpass.setObjectName("le_newpass")
        self.verticalLayout.addWidget(self.le_newpass)
        self.label_newpass_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_newpass_2.setFont(font)
        self.label_newpass_2.setObjectName("label_newpass_2")
        self.verticalLayout.addWidget(self.label_newpass_2)
        self.le_Cnewpass = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_Cnewpass.setFont(font)
        self.le_Cnewpass.setObjectName("le_Cnewpass")
        self.verticalLayout.addWidget(self.le_Cnewpass)
        self.reset_btn = QtWidgets.QPushButton(Dialog)
        self.reset_btn.setGeometry(QtCore.QRect(70, 350, 141, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.reset_btn.clicked.connect(self.after_reset)
        self.reset_btn.clicked.connect(Dialog.close)




        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_Uname.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">User Name</span></p></body></html>"))
        self.label_prepass.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Previous Password</span></p></body></html>"))
        self.label_newpass.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">New Password</span></p></body></html>"))
        self.label_newpass_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Confirm New Password</span></p></body></html>"))
        self.reset_btn.setText(_translate("Dialog", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
