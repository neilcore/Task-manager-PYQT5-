import sqlite3
import sys
from PyQt5.QtCore import QDateTime, Qt

def displayDatas():

	conn = sqlite3.connect('TaskManagerDB.db')
	cursor = conn.cursor()

	table = """CREATE TABLE IF NOT EXISTS taskLIST(row_no INTEGER PRIMARY KEY,task_name TEXT, task_schedule TEXT,task_note TEXT)"""
	cursor.execute(table)
	
	cursor.execute("SELECT task_name, task_schedule, task_note FROM taskLIST")
	dataTuple = cursor.fetchall()

	return dataTuple

	conn.close()


def MarkAsDone(itemAsDone):
	filename = 'AccomplishedTask.txt'

	with open(filename, 'a') as fl_obj:
		fl_obj.write(itemAsDone)

def deleteselecteditem(selectedItem):
	filename = 'deletedTasks.txt'
	conn = sqlite3.connect('TaskManagerDB.db')
	cursor = conn.cursor()

	cursor.execute("SELECT task_name FROM taskLIST")
	allItems = cursor.fetchall()

	for tuple in allItems:
		for dlt in tuple:
			if dlt in selectedItem:
				cursor.execute("DELETE FROM taskLIST WHERE task_name = '" + dlt + "'")
				conn.commit()

	with open(filename, 'a') as fl_obj:
		fl_obj.write(selectedItem)

	conn.close()

def deletealldatafromtable():
	conn = sqlite3.connect('TaskManagerDB.db')
	cursor = conn.cursor()

	cursor.execute("DELETE FROM taskLIST")
	conn.commit()

	conn.close()

def displaylastrow():
	conn = sqlite3.connect('TaskManagerDB.db')
	cursor = conn.cursor()

	cursor.execute("SELECT COUNT(*) FROM taskLIST")
	norows = cursor.fetchone()

	for i in norows:
		if i == 1:
			cursor.execute("SELECT task_name, task_schedule, task_note FROM taskLIST")
			items = cursor.fetchall()
			return items
		else:
			cursor.execute("SELECT task_name, task_schedule, task_note FROM taskLIST ORDER BY row_no DESC LIMIT 1")
			lastrow = cursor.fetchall()
			return lastrow

	conn.close()

def storedatas(taskn, taskSched, tasknote=''):
	conn = sqlite3.connect('TaskManagerDB.db')
	cursor = conn.cursor()

	cursor.execute("INSERT INTO taskLIST(task_name,task_schedule,task_note) values(?,?,?)",(taskn,taskSched,tasknote))
	conn.commit()

	conn.close()

