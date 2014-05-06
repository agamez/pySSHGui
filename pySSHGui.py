#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pySSHGui_ui
import sys

class PySSHGui(QMainWindow, pySSHGui_ui.Ui_MainWindow):
	def __init__(self, parent=None):
		super(PySSHGui, self).__init__(parent)
		self.setupUi(self)

	def on_newButton_clicked(self, b):
		print "Clicked new button"

	def on_editButton_clicked(self, b):
		print "Clicked edit button"

	def on_removeButton_clicked(self, b):
		print "Clicked remove button"

	def on_connectButton_clicked(self, b):
		print "Clicked connect button"


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = PySSHGui()
	form.show()
	app.exec_()

