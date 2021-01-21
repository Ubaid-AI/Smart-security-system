from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import call
#from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):

    def on_clicked(self):
        call(["python","Login.py"])

    def on_clicked1(self):
        call(["python","InsertWin.py"])

    def on_clicked2(self):
        call(["python","Update.py"])

    def on_clicked3(self):
        call(["python","Delete.py"])

    def on_clicked4(self):
        call(["python","ViewWin.py"])

    def on_clicked5(self):
        call(["python", "AboutDev.py"])

    def on_clicked6(self):
        call(["python","Features.py"])

    def on_clicked7(self):
        call(["python", "facerecog_from_webcam(improved).py"])

    def detector_h(self):
        call(["python", "detector.py", ])

    def Setting(self):
        call(["python", "Setting.py"])

    def about(self):
        call(["python", "About.py"])

    def ask(self):

        msg = QMessageBox()
        msg.setWindowTitle(" All RECORDS ")
        msg.setText(" Do You Want To Open Student Records ")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Open |QMessageBox.Ignore | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.setInformativeText(" Read Details Carefully ")
        msg.setDetailedText(" If You Press Ignore You Will Be Rediret To Faculty Records Otherwise You May Press Cancel To Remain On This Page ")
        msg.buttonClicked.connect(self.decision)

        x = msg.exec_()


    def decision(self, i):

      if(i.text() == 'Open'):

        call(["python","ShowStudent.py"])


      elif(i.text() == 'Ignore'):

          call(["python","ShowFaculty.py"])




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 580)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 170, 351, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.insert = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.insert.setMinimumSize(QtCore.QSize(0, 30))
        self.insert.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.insert.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insert.setIcon(icon)
        self.insert.setIconSize(QtCore.QSize(30, 30))
        self.insert.setObjectName("insert")
        self.insert.clicked.connect(MainWindow.close)
        self.insert.clicked.connect(self.on_clicked1)

##########################################################################
        self.gridLayout.addWidget(self.insert, 0, 0, 1, 1)
        self.delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.delete.setMinimumSize(QtCore.QSize(0, 30))
        self.delete.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete.setIcon(icon1)
        self.delete.setIconSize(QtCore.QSize(28, 28))
        self.delete.setObjectName("delete")
        self.delete.clicked.connect(MainWindow.close)
        self.delete.clicked.connect(self.on_clicked3)

##########################################################################

        self.gridLayout.addWidget(self.delete, 1, 0, 1, 1)

        self.View = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.View.setMinimumSize(QtCore.QSize(0, 30))
        self.View.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.View.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.View.setIcon(icon2)
        self.View.setIconSize(QtCore.QSize(25, 25))
        self.View.setObjectName("View")
        self.View.clicked.connect(MainWindow.close)
        self.View.clicked.connect(self.on_clicked4)

##########################################################################

        self.gridLayout.addWidget(self.View, 1, 1, 1, 1)
        self.update = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.update.setMinimumSize(QtCore.QSize(0, 30))
        self.update.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.update.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update.setIcon(icon3)
        self.update.setIconSize(QtCore.QSize(30, 25))
        self.update.setObjectName("update")
        self.update.clicked.connect(MainWindow.close)
        self.update.clicked.connect(self.on_clicked2)

#############################################################################

        self.gridLayout.addWidget(self.update, 0, 1, 1, 1)
        self.btn_Show = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_Show.setMinimumSize(QtCore.QSize(0, 30))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Show.setIcon(icon4)
        self.btn_Show.setIconSize(QtCore.QSize(25, 20))
        self.btn_Show.setObjectName("btn_Show")
        self.btn_Show.clicked.connect(self.ask)
        self.gridLayout.addWidget(self.btn_Show, 2, 0, 1, 1)
        self.btn_live = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_live.setMinimumSize(QtCore.QSize(0, 30))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_live.setIcon(icon5)
        self.btn_live.setIconSize(QtCore.QSize(25, 20))
        self.btn_live.setObjectName("btn_live")
        self.btn_live.clicked.connect(MainWindow.close)
        self.btn_live.clicked.connect(self.on_clicked6)
        self.gridLayout.addWidget(self.btn_live, 2, 1, 1, 1)
        self.label_Logo = QtWidgets.QLabel(self.centralwidget)
        self.label_Logo.setGeometry(QtCore.QRect(0, 0, 111, 101))
        self.label_Logo.setText("")
        self.label_Logo.setPixmap(QtGui.QPixmap("images/Logo.png"))
        self.label_Logo.setScaledContents(True)
        self.label_Logo.setObjectName("label_Logo")
        self.label_Title = QtWidgets.QLabel(self.centralwidget)
        self.label_Title.setGeometry(QtCore.QRect(110, 10, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_Title.setFont(font)
        self.label_Title.setObjectName("label_Title")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setGeometry(QtCore.QRect(-10, -8, 819, 550))
        self.BG.setText("")
        self.BG.setPixmap(QtGui.QPixmap("images/BG2.png"))
        self.BG.setScaledContents(True)
        self.BG.setObjectName("BG")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 140, 190, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


  ###################################################################################

        self.BG.raise_()
        self.gridLayoutWidget.raise_()
        self.label_Logo.raise_()
        self.label_Title.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuCamera = QtWidgets.QMenu(self.menubar)
        self.menuCamera.setObjectName("menuCamera")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCamera_1 = QtWidgets.QAction(MainWindow)
        self.actionCamera_1.setObjectName("actionCamera_1")
        self.actionCamera_2 = QtWidgets.QAction(MainWindow)
        self.actionCamera_2.setObjectName("actionCamera_2")
        self.actionCamera_3 = QtWidgets.QAction(MainWindow)
        self.actionCamera_3.setObjectName("actionCamera_3")
        self.actionLog_out = QtWidgets.QAction(MainWindow)
        self.actionLog_out.setObjectName("actionLog_out")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_System = QtWidgets.QAction(MainWindow)
        self.actionAbout_System.setObjectName("actionAbout_System")
        self.actionAbout_Developers = QtWidgets.QAction(MainWindow)
        self.actionAbout_Developers.setObjectName("actionAbout_Developers")
        self.menuCamera.addAction(self.actionCamera_1)
        self.menuCamera.addAction(self.actionCamera_2)
        self.menuMain.addAction(self.actionSettings)
        self.menuMain.addAction(self.actionLog_out)
        self.menuAbout.addAction(self.actionAbout_System)
        self.menuAbout.addAction(self.actionAbout_Developers)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuCamera.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.actionCamera_1.triggered.connect(self.on_clicked7)
        self.actionCamera_2.triggered.connect(self.detector_h)
        self.actionSettings.triggered.connect(self.Setting)
        self.actionLog_out.triggered.connect(MainWindow.close)
        self.actionLog_out.triggered.connect(self.on_clicked)
        self.actionAbout_System.triggered.connect(self.about)
        self.actionAbout_Developers.triggered.connect(self.on_clicked5)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.insert.setText(_translate("MainWindow", "Insert"))
        self.delete.setText(_translate("MainWindow", "Delete"))
        self.View.setText(_translate("MainWindow", "View"))
        self.update.setText(_translate("MainWindow", "Update"))
        self.btn_Show.setText(_translate("MainWindow","Show Database"))
        self.btn_live.setText(_translate("MainWindow","Live Feed"))
        self.label_Title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Smart Security System</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#066f95;\">Manage Entities</span></p></body></html>"))
        self.menuCamera.setTitle(_translate("MainWindow", "Camera"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionCamera_1.setText(_translate("MainWindow", "Camera 1"))
        self.actionCamera_2.setText(_translate("MainWindow", "Camera 2"))
        self.actionLog_out.setText(_translate("MainWindow", "Log out"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionAbout_Developers.setText(_translate("MainWindow", "About Developer"))
        self.actionAbout_System.setText(_translate("MainWindow", "About System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
