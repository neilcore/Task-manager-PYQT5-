from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
from AdditionalOperations import *
from DatabaseA import *
from Main import *
import multiprocessing

class Form(QMainWindow):
	def __init__(self):
		super(). __init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.systemdatetime = QDateTime.currentDateTime()
		self.ui.dateTimeEditWIGET.setDisplayFormat("dd/MM/yyyy h:mm AP")

		displayitems(self.ui)

		self.ui.pushbuttonFORSAVE.clicked.connect(self.savebutton)
		self.ui.pushButtonFORMARKASDONE.clicked.connect(self.markasdone)
		self.ui.actionDelete_All_Task_List.triggered.connect(self.deletealltask)
		self.ui.pushButtonFORDELETE.clicked.connect(self.deleteitem)
		self.ui.actionExit.triggered.connect(self.CExit)
		self.ui.pushButtonFORDELETEALL.clicked.connect(self.deletealltask)
		self.show()

	def CExit(self):
		self.close()
	def deleteitem(self):
		selecteditem = self.ui.listWidget_fortaskList.currentItem().text()
		self.ui.listWidget_fortaskList.takeItem(self.ui.listWidget_fortaskList.currentRow())
		deleteselecteditem(selecteditem)
	def deletealltask(self):
		self.ui.listWidget_fortaskList.clear()
		deletealldatafromtable()
	def markasdone(self):
		
		selectedItem = self.ui.listWidget_fortaskList.currentItem().text()
		self.ui.listWidget_fortaskList.takeItem(self.ui.listWidget_fortaskList.currentRow())
		MarkAsDone(selectedItem)
		markasdone(selectedItem)
	def savebutton(self):
		taskname = self.ui.lineEdit_fortaskname.text()
		sched = self.ui.dateTimeEditWIGET.dateTime().toString(Qt.DefaultLocaleLongDate)

		if self.ui.lineEdit_forNote.text() == "":
			self.ui.lineEdit_forNote.setText("No Description Added")

		note = self.ui.lineEdit_forNote.text()
		if self.ui.lineEdit_fortaskname.text() != "":

			if self.ui.dateTimeEditWIGET.dateTime() >= self.systemdatetime:
				storedatas(taskname,sched,note)
				lastrow = displaylastrow()
				displayLastRow(self.ui, lastrow)
				self.ui.lineEdit_forNote.clear()
				self.ui.lineEdit_fortaskname.clear()
			else:
				scheduleErrorMsgBox()
		else:
			tasknameErrorMsgBox()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = Form()
	w.show()
	sys.exit(app.exec_())