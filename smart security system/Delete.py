import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import call
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Arbaz123", database="mydb")
conn = mydb.cursor()


class Ui_DeleteWin(object):

    def on_clicked1(self):
        call(["python","MainWindow.py"])

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


    def check_std(self):

      field = self.search_le.text()

      query = """SELECT COUNT(*) FROM StudentData WHERE Std_ID = %s"""
      res = (field,)
      conn.execute(query, res)
      val = conn.fetchone()
      return val[0]


    def check_emp(self):

       field = self.search_le.text()

       query = """SELECT COUNT(*) FROM StaffData WHERE Emp_ID = %s"""
       res = (field,)
       conn.execute(query, res)
       val = conn.fetchone()
       return val[0]



    def before_search(self):

        if (len(self.search_le.text())) <1:
            self.pop_window('Enter ID Here !')

        else:

           check1 = self.check_std()
           check2 = self.check_emp()

           if (check1 == 1) and (check2 == 0):

                self.send_std()

           elif (check1 == 0) and (check2 == 1):

                self.send_emp()

           else:
               self.pop_window('No User Found Of This ID')


    def send_std(self):

        field = self.search_le.text()

        query = """SELECT * FROM StudentData WHERE Std_ID = %s"""
        res = (field,)
        conn.execute(query, res)
        val = conn.fetchall()
        for z in val:

            if (field == z[0]):
                name = z[1]
                dept = z[2]
                mail = z[3]

                std = "S"
                Ui_DeleteWin.search(self, field, name, dept, mail, std)
                break


    def send_emp(self):

        field = self.search_le.text()
        query = """SELECT * FROM StaffData WHERE Emp_ID = %s"""
        res = (field,)
        conn.execute(query, res)
        val = conn.fetchall()
        for z in val:

            if (field == z[0]):
                name = z[1]
                dept = z[2]
                mail = z[3]

                emp = "E"
                Ui_DeleteWin.search(self, field, name, dept, mail, emp)
                break


    def delete1(self):

        Id = self.ID_le.text()
        name = self.Name_le.text()
        dept = self.dept_le.text()
        mail = self.email_le.text()
        # print(Id)
        querry = """DELETE FROM StudentData WHERE Std_Id = %s"""
        value = (Id,)
        conn.execute(querry, value)
        mydb.commit()
        self.pop_window2("Record Deleted Successfully.")

    def delete2(self):

        Id = self.ID_le.text()
        name = self.Name_le.text()
        dept = self.dept_le.text()
        mail = self.email_le.text()
        # print(Id)
        querry = """DELETE FROM StaffData WHERE Emp_Id = %s"""
        value = (Id,)
        conn.execute(querry, value)
        mydb.commit()
        self.pop_window2("Record Deleted Successfully.")
        self.ID_le.clear()
        self.Name_le.clear()
        self.dept_le.clear()
        self.email_le.clear()

    def search(self, roll, name, dept, mail, find):


        self.btn_search.close()
        self.verticalLayoutWidget.close()
        _translate = QtCore.QCoreApplication.translate


        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(20, 250, 169, 30))
        self.btn_delete.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_delete.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_delete.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon1)
        self.btn_delete.setIconSize(QtCore.QSize(30, 30))
        self.btn_delete.setObjectName("btn_delete")

        if find == 'S':
         self.btn_delete.clicked.connect(self.delete1)

        if find == 'E':
            self.btn_delete.clicked.connect(self.delete2)

        self.btn_delete.setText(_translate("Delete", "Delete"))
        self.btn_delete.raise_()
        self.btn_delete.show()

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 150, 351, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.InsetGLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.InsetGLayout.setContentsMargins(0, 0, 0, 0)
        self.InsetGLayout.setHorizontalSpacing(5)
        self.InsetGLayout.setObjectName("InsetGLayout")
        self.std_ID = QtWidgets.QLabel(self.gridLayoutWidget)
        self.std_ID.setObjectName("std_ID")
        self.InsetGLayout.addWidget(self.std_ID, 0, 0, 1, 1)
        self.email_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.email_le.setObjectName("email_le")
        self.email_le.setText(mail)
        self.InsetGLayout.addWidget(self.email_le, 3, 2, 1, 1)
        self.Std_Dept = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Std_Dept.setObjectName("Std_Dept")
        self.InsetGLayout.addWidget(self.Std_Dept, 2, 0, 1, 1)
        self.std_Name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.std_Name.setObjectName("std_Name")
        self.InsetGLayout.addWidget(self.std_Name, 1, 0, 1, 1)
        self.dept_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.dept_le.setObjectName("dept_le")
        self.dept_le.setText(dept)
        self.InsetGLayout.addWidget(self.dept_le, 2, 2, 1, 1)
        self.Std_email = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Std_email.setObjectName("Std_email")
        self.InsetGLayout.addWidget(self.Std_email, 3, 0, 1, 1)
        self.upload_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.upload_label.setObjectName("upload_label")
        self.InsetGLayout.addWidget(self.upload_label, 4, 0, 1, 1)
        self.ID_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ID_le.setObjectName("ID_le")
        self.ID_le.setText(roll)
        self.InsetGLayout.addWidget(self.ID_le, 0, 2, 1, 1)
        self.Name_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Name_le.setObjectName("Name_le")
        self.Name_le.setText(name)
        self.InsetGLayout.addWidget(self.Name_le, 1, 2, 1, 1)
        self.upload_btn = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.upload_btn.setObjectName("upload_btn")
        self.InsetGLayout.addWidget(self.upload_btn, 4, 1, 1, 1)
        self.img_le = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img_le.setText("")
        self.img_le.setObjectName("img_le")
        self.InsetGLayout.addWidget(self.img_le, 4, 2, 1, 1)
        self.gridLayoutWidget.raise_()
        self.gridLayoutWidget.show()

        self.std_ID.setText(_translate("Delete","<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">User ID</span></p></body></html>"))
        self.Std_Dept.setText(_translate("Delete","<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Department</span></p></body></html>"))
        self.std_Name.setText(_translate("Delete","<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Name</span></p></body></html>"))
        self.Std_email.setText(_translate("Delete","<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">E-mail</span></p></body></html>"))
        self.upload_label.setText(_translate("Delete","<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Upload Image</span></p></body></html>"))
        self.SubT_label.setText(_translate("Delete","<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#066f95;\">Delete Record</span></p></body></html>"))


    def setupUi(self, DeleteWin):
        DeleteWin.setObjectName("DeleteWin")
        DeleteWin.resize(800, 580)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeleteWin.sizePolicy().hasHeightForWidth())
        DeleteWin.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(DeleteWin)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Logo = QtWidgets.QLabel(self.centralwidget)
        self.label_Logo.setGeometry(QtCore.QRect(0, 0, 111, 101))
        self.label_Logo.setText("")
        self.label_Logo.setPixmap(QtGui.QPixmap("images/Logo.png"))
        self.label_Logo.setScaledContents(True)
        self.label_Logo.setObjectName("label_Logo")
        self.label_Title = QtWidgets.QLabel(self.centralwidget)
        self.label_Title.setGeometry(QtCore.QRect(110, 10, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_Title.setFont(font)
        self.label_Title.setObjectName("label_Title")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setGeometry(QtCore.QRect(-10, -8, 819, 550))
        self.BG.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BG.setFont(font)
        self.BG.setText("")
        self.BG.setPixmap(QtGui.QPixmap("images/BG2.png"))
        self.BG.setScaledContents(True)
        self.BG.setObjectName("BG")
        self.SubT_label = QtWidgets.QLabel(self.centralwidget)
        self.SubT_label.setGeometry(QtCore.QRect(320, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.SubT_label.setFont(font)
        self.SubT_label.setObjectName("SubT_label")

        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(680, 30, 80, 30))
        self.exit.setMinimumSize(QtCore.QSize(80, 30))
        self.exit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.exit.setSizeIncrement(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon1)
        self.exit.setIconSize(QtCore.QSize(50, 70))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(DeleteWin.close)
        self.exit.clicked.connect(self.on_clicked1)

        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(10, 250, 189, 30))
        self.btn_search.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_search.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_search.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon2)
        self.btn_search.setObjectName("btn_search")
        self.btn_search.clicked.connect(self.before_search)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(229, 220, 331, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_search = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_search.setObjectName("label_search")
        self.verticalLayout.addWidget(self.label_search)
        self.search_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.search_le.setMinimumSize(QtCore.QSize(0, 30))
        self.search_le.setObjectName("search_le")
        self.search_le.setPlaceholderText(" Ex: 20XX-XX-XXX ")

        self.verticalLayout.addWidget(self.search_le)
        self.BG.raise_()
        self.label_Logo.raise_()
        self.label_Title.raise_()
        self.SubT_label.raise_()
        self.exit.raise_()
        self.btn_search.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(DeleteWin)
        QtCore.QMetaObject.connectSlotsByName(DeleteWin)

    def retranslateUi(self, DeleteWin):
        _translate = QtCore.QCoreApplication.translate
        DeleteWin.setWindowTitle(_translate("DeleteWin", "MainWindow"))
        self.label_Title.setText(_translate("DeleteWin", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Smart Security System</span></p></body></html>"))
        self.SubT_label.setText(_translate("DeleteWin", "<html><head/><body><p align=\"justify\"><span style=\" font-size:16pt; font-weight:600; color:#066f95;\">Search Record</span></p></body></html>"))
        self.exit.setText(_translate("DeleteWin", "Exit"))
        self.btn_search.setText(_translate("DeleteWin", "Search"))
        self.label_search.setText(_translate("DeleteWin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Enter ID ""</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteWin = QtWidgets.QDialog()
    ui = Ui_DeleteWin()
    ui.setupUi(DeleteWin)
    DeleteWin.show()
    sys.exit(app.exec_())