from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QDateTime, Qt
from DatabaseA import *
import sqlite3

def scheduleErrorMsgBox():
	msg = QMessageBox()
	msg.setWindowTitle("Invalid Schedule!")
	msg.setText("The Schedule you provided is Invalid.")
	msg.setIcon(QMessageBox.Critical)
	msg.setDetailedText("The provided schedule is Invalid. maybe the provided schedule is behind the current Date and Time. Please try to check again")
	x = msg.exec_()

def tasknameErrorMsgBox():
	msg = QMessageBox()
	msg.setWindowTitle("Task Name Error")
	msg.setText("Enter your Task Name.")
	msg.setIcon(QMessageBox.Information)
	msg.setDetailedText("It is required to provide a Task Name")
	x = msg.exec_()

def displayitems(Ui):
	datas = displayDatas()

	for tuple in datas:
		items = QtWidgets.QListWidgetItem("\t\t".join(tuple))
		Ui.listWidget_fortaskList.addItem(items)

def displayLastRow(Ui, lastrow):
	for tuple in lastrow:
		items = QtWidgets.QListWidgetItem("\t\t".join(tuple))
		Ui.listWidget_fortaskList.addItem(items)
def markasdone(theitem):

	conn = sqlite3.connect('TaskManagerDB.db')
	cursor = conn.cursor()

	table = """CREATE TABLE IF NOT EXISTS taskLIST(row_no INTEGER PRIMARY KEY,task_name TEXT, task_schedule TEXT,task_note TEXT)"""
	cursor.execute(table)

	cursor.execute("SELECT task_name FROM taskLIST")
	allItems = cursor.fetchall()

	for tuple in allItems:
		for i in tuple:
			if i in theitem:
				cursor.execute("DELETE FROM taskLIST WHERE task_name = '" + i + "'")
				conn.commit()

	conn.close()

#item = QtWidgets.QListWidgetItem(Ui.listWidget_fortaskList.item(index))