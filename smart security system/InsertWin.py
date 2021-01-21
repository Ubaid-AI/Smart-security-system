
from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import call
#from MainWindow import *
import tkinter as tk
from tkinter import filedialog
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Arbaz123", database="mydb")
conn = mydb.cursor()


class Ui_InsertWin(object):

    def __init__(self) -> None:
        super().__init__()


    def on_clicked1(self):
        call(["python", "MainWindow.py"])

    def clear_le(self):
        self.ID_le.clear()
        self.Name_le.clear()
        self.dept_le.clear()
        self.email_le.clear()
        self.img_le.clear()

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



    def ChangeToEmp(self):
        self.insert_std.close()
        _translate = QtCore.QCoreApplication.translate
        self.std_ID.setText(_translate("InsertWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Employe ID</span></p></body></html>"))
        self.insert_emp = QtWidgets.QPushButton(self.centralwidget)
        self.insert_emp.setGeometry(QtCore.QRect(20, 250, 169, 30))
        self.insert_emp.setMinimumSize(QtCore.QSize(0, 30))
        self.insert_emp.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.insert_emp.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insert_emp.setIcon(icon1)
        self.insert_emp.setIconSize(QtCore.QSize(30, 30))
        self.insert_emp.setObjectName("insert_emp")
        self.insert_emp.clicked.connect(self.emp_insert)
        self.insert_emp.setText(_translate("InsertWin", "Insert Employe"))
        self.insert_emp.raise_()
        self.insert_emp.show()
        self.ID_le.clear()
        self.Name_le.clear()
        self.dept_le.clear()
        self.email_le.clear()
        self.img_le.clear()

    def ChangeToStd(self):
        self.insert_emp.close()
        self.insert_std.show()
        _translate = QtCore.QCoreApplication.translate
        self.std_ID.setText(_translate("InsertWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Student ID</span></p></body></html>"))
        self.ID_le.clear()
        self.Name_le.clear()
        self.dept_le.clear()
        self.email_le.clear()
        self.img_le.clear()

    def after_upload(self):

        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetype = (("png","*.png"),("jpeg",".jpg")))
        root.destroy()
        self.path = self.filename
        self.img_le.setPixmap(QtGui.QPixmap(self.path))
        self.img_le.setScaledContents(True)
        #self.pop_window('All Fields Are Required !')

    def std_insert(self):

        roll = self.ID_le.text()
        name = self.Name_le.text()
        dept = self.dept_le.text()
        mail = self.email_le.text()
        paths = self.path

        querry = """INSERT INTO StudentData(Std_ID, Std_Name, Department, Email, Image)  VALUES (%s, %s, %s, %s, %s)"""

        Img = Ui_InsertWin.ConvertImage(self, paths)
        Data_tuple = (roll, name, dept, mail, Img)
        conn.execute(querry, Data_tuple)
        mydb.commit()
        self.pop_window2('Student Inserted Succesfully !')


    def emp_insert(self):

        roll = self.ID_le.text()
        name = self.Name_le.text()
        dept = self.dept_le.text()
        mail = self.email_le.text()
        paths = self.path

        querry = """INSERT INTO StaffData(Emp_ID, Emp_Name, Emp_Dept, Emp_Email, Emp_Image)  VALUES (%s, %s, %s, %s, %s)"""

        Img = Ui_InsertWin.ConvertImage(self, paths)
        Data_tuple = (roll, name, dept, mail, Img)
        conn.execute(querry, Data_tuple)
        mydb.commit()
        self.pop_window2('Employ Inserted Succesfully !')



    def ConvertImage(self, paths):
        with open(paths, 'rb') as f:
            binary = f.read()
        return binary

    def setupUi(self, InsertWin):
        InsertWin.setObjectName("InsertWin")
        InsertWin.resize(800, 580)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InsertWin.sizePolicy().hasHeightForWidth())
        InsertWin.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(InsertWin)
        self.centralwidget.setObjectName("centralwidget")
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
        # self.Name_le.setText(email)

        ################################################################

        self.InsetGLayout.addWidget(self.email_le, 3, 2, 1, 1)
        self.Std_Dept = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Std_Dept.setObjectName("Std_Dept")
        self.InsetGLayout.addWidget(self.Std_Dept, 2, 0, 1, 1)
        self.std_Name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.std_Name.setObjectName("std_Name")
        self.InsetGLayout.addWidget(self.std_Name, 1, 0, 1, 1)
        self.dept_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.dept_le.setObjectName("dept_le")
        # self.Name_le.setText(dept)

        ###############################################################

        self.InsetGLayout.addWidget(self.dept_le, 2, 2, 1, 1)
        self.Std_email = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Std_email.setObjectName("Std_email")
        self.InsetGLayout.addWidget(self.Std_email, 3, 0, 1, 1)
        self.upload_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.upload_label.setObjectName("upload_label")
        self.InsetGLayout.addWidget(self.upload_label, 4, 0, 1, 1)
        self.ID_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ID_le.setObjectName("ID_le")

        ##############################################################

        self.InsetGLayout.addWidget(self.ID_le, 0, 2, 1, 1)
        self.Name_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Name_le.setObjectName("Name_le")

        ######################################################################

        self.InsetGLayout.addWidget(self.Name_le, 1, 2, 1, 1)
        self.upload_btn = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.upload_btn.setObjectName("upload_btn")
        self.upload_btn.clicked.connect(self.after_upload)
        #####################################################################

        self.InsetGLayout.addWidget(self.upload_btn, 4, 1, 1, 1)
        self.img_le = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img_le.setText("")
        self.img_le.setObjectName("img_le")
        self.InsetGLayout.addWidget(self.img_le, 4, 2, 1, 1)
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
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BG.setFont(font)
        self.BG.setText("")
        self.BG.setPixmap(QtGui.QPixmap("images/BG2.png"))
        self.BG.setScaledContents(True)
        self.BG.setObjectName("BG")
        self.SubT_label = QtWidgets.QLabel(self.centralwidget)
        self.SubT_label.setGeometry(QtCore.QRect(300, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.SubT_label.setFont(font)
        self.SubT_label.setObjectName("SubT_label")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(598, 250, 191, 30))
        self.clear_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_btn.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clear_btn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_btn.setIcon(icon)
        self.clear_btn.setIconSize(QtCore.QSize(28, 28))
        self.clear_btn.setObjectName("clear_btn")

        ########################################################################

        self.clear_btn.clicked.connect(self.clear_le)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 440, 431, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.student_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.student_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.student_btn.setFont(font)
        self.student_btn.setObjectName("student_btn")



        #####################################################################

        self.student_btn.clicked.connect(self.ChangeToStd)
        self.horizontalLayout.addWidget(self.student_btn)
        self.emp_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.emp_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.emp_btn.setFont(font)
        self.emp_btn.setObjectName("emp_btn")

        #####################################################################

        self.emp_btn.clicked.connect(self.ChangeToEmp)
        self.horizontalLayout.addWidget(self.emp_btn)
        self.insert_std = QtWidgets.QPushButton(self.centralwidget)
        self.insert_std.setGeometry(QtCore.QRect(20, 250, 169, 30))
        self.insert_std.setMinimumSize(QtCore.QSize(0, 30))
        self.insert_std.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.insert_std.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insert_std.setIcon(icon1)
        self.insert_std.setIconSize(QtCore.QSize(30, 30))
        self.insert_std.setObjectName("insert_std")
        self.insert_std.clicked.connect(self.std_insert)

        #############################################################################

        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(680, 30, 80, 30))
        self.exit.setMinimumSize(QtCore.QSize(80, 30))
        self.exit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.exit.setSizeIncrement(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon2)
        self.exit.setIconSize(QtCore.QSize(50, 70))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(InsertWin.close)
        self.exit.clicked.connect(self.on_clicked1)

        #########################################################################

        self.BG.raise_()
        self.gridLayoutWidget.raise_()
        self.label_Logo.raise_()
        self.label_Title.raise_()
        self.SubT_label.raise_()
        self.clear_btn.raise_()
        self.horizontalLayoutWidget.raise_()
        self.insert_std.raise_()
        self.exit.raise_()

        self.retranslateUi(InsertWin)
        QtCore.QMetaObject.connectSlotsByName(InsertWin)

    def retranslateUi(self, InsertWin):
        _translate = QtCore.QCoreApplication.translate
        InsertWin.setWindowTitle(_translate("InsertWin", "MainWindow"))
        self.std_ID.setText(_translate("InsertWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Student ID</span></p></body></html>"))
        self.Std_Dept.setText(_translate("InsertWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Department</span></p></body></html>"))
        self.std_Name.setText(_translate("InsertWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Name</span></p></body></html>"))
        self.Std_email.setText(_translate("InsertWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">E-mail</span></p></body></html>"))
        self.upload_label.setText(_translate("InsertWin", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Upload Image</span></p></body></html>"))
        self.upload_btn.setText(_translate("InsertWin", "..."))
        self.label_Title.setText(_translate("InsertWin", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Smart Security System</span></p></body></html>"))
        self.SubT_label.setText(_translate("InsertWin", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#066f95;\">Insert New Entity</span></p></body></html>"))
        self.clear_btn.setText(_translate("InsertWin", "Clear"))
        self.student_btn.setText(_translate("InsertWin", "Student"))
        self.emp_btn.setText(_translate("InsertWin", "Employe"))
        self.insert_std.setText(_translate("InsertWin", "Insert Student"))

if __name__ == "__main__":
    import sys
    root = tk.Tk()
    app = QtWidgets.QApplication(sys.argv)
    InsertWin = QtWidgets.QDialog()
    ui = Ui_InsertWin()
    ui.setupUi(InsertWin)
    InsertWin.show()
    sys.exit(app.exec_())
