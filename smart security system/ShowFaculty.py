from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os.path
import mysql.connector
import base64

class Ui_MainWindow(QtWidgets.QMainWindow):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UI_FILE = os.path.join(BASE_DIR, "Emp_Design.ui")


    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        uic.loadUi(self.UI_FILE, self)
        self.readBtn.clicked.connect(self.showTableData)

    def showTableData(self):

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Arbaz123", database="mydb")
        conn = mydb.cursor()
        conn.execute("SELECT * FROM StaffData")
        val = conn.fetchall()

        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(val):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):

                item = str(column_data)

                if (column_number == 5):
                    item = self.getImage(column_data)
                    self.tableWidget.setCellWidget(row_number, column_number, item)
                else:
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(item)))
                    # self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
                    self.tableWidget.verticalHeader().setDefaultSectionSize(100)

    def getImageLabel(self, column_data):


        imageLabel = QtWidgets.QLabel(self.centralwidget)
        imageLabel.setText("")
        imageLabel.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        data = base64.b64encode(column_data)
        pixmap.loadFromData(data, 'png')
        imageLabel.setPixmap(pixmap)
        return imageLabel





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
