#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pySSHGui_ui
from ssh_config import SSH_Config

import sys


class PySSHGui(QMainWindow, pySSHGui_ui.Ui_MainWindow):
	def __init__(self, ssh_config):
		super(PySSHGui, self).__init__()
		self.setupUi(self)
		self.ssh_config = ssh_config

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
	form = PySSHGui(SSH_Config())
	form.show()
	app.exec_()

