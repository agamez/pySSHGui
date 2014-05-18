#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pySSHGui_ui
from ssh_config import SSH_Config

import sys
import os

class PySSHGui(QMainWindow, pySSHGui_ui.Ui_MainWindow):
	def __init__(self, ssh_config):
		super(PySSHGui, self).__init__()
		self.setupUi(self)
		self.ssh_config = ssh_config

		self.hostRadioButtons = list()
		for host in self.ssh_config.hosts:
			print host

			self.hostRadioButtons.append(QRadioButton(self.centralwidget))
			self.hostRadioButtons[-1].setObjectName(host["Host"])
			self.hostRadioButtons[-1].setText(host["Host"])
			self.hostRadioButtons[-1]._associated_ssh_host = host
			self.hostsLayout.addWidget(self.hostRadioButtons[-1])


	def on_newButton_clicked(self, b):
		print "Clicked new button"

	def on_editButton_clicked(self, b):
		print "Clicked edit button"

	def on_removeButton_clicked(self, b):
		print "Clicked remove button"
		for button in self.hostRadioButtons:
			if button.isChecked():
				self.ssh_config.hosts.remove(button._associated_ssh_host)
				self.hostsLayout.removeWidget(button)
				self.hostRadioButtons.remove(button)
				button.setParent(None)
		self.ssh_config.save()

	def on_connectButton_clicked(self, b):
		print "Clicked connect button"
		for button in self.hostRadioButtons:
			if button.isChecked():
				#ssh_command = "x-terminal-emulator -e ssh %s" % button._associated_ssh_host["Host"]
				ssh_command = 'osso-xterm -e "ssh %s"' % button._associated_ssh_host["Host"]
				os.system(ssh_command)
				break


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = PySSHGui(SSH_Config())
	form.show()
	app.exec_()

