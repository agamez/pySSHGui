#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pySSHGui_ui
import editHost_ui
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
			self.addHost(host)

	def addHost(self, host):
		print host

		self.hostRadioButtons.append(QRadioButton(self.centralwidget))
		self.hostRadioButtons[-1].setObjectName(host["Host"])
		self.hostRadioButtons[-1].setText(host["Host"])
		self.hostRadioButtons[-1]._associated_ssh_host = host
		self.hostsLayout.addWidget(self.hostRadioButtons[-1])

	def get_checkedButton(self):
		for button in self.hostRadioButtons:
			if button.isChecked():
				return button
		return None

	def on_newButton_clicked(self, b):
		editHost = QDialog()
		ui = editHost_ui.Ui_editHost()
		ui.setupUi(editHost)
		editHost.setWindowTitle('New host')
		if editHost.exec_():
			new_host = {'Host' : str(ui.Name.text()),
				    'HostName' : str(ui.HostName.text()),
				    'User' : str(ui.User.text()),
				    'Port' : str(ui.Port.text()),
				    'IdentityFile' : str(ui.IdentityFile.text())
				    }
			print new_host
			self.ssh_config.hosts.append(new_host)
			self.ssh_config.save()
			self.addHost(new_host)

		print "Clicked new button"

	def on_editButton_clicked(self, b):
		editHost = QDialog()
		ui = editHost_ui.Ui_editHost()
		ui.setupUi(editHost)
		editHost.setWindowTitle('Edit host')

		button = self.get_checkedButton()

		ui.Name.setText(button._associated_ssh_host['Host'])
		ui.HostName.setText(button._associated_ssh_host['HostName'])
		ui.User.setText(button._associated_ssh_host['User'])
		ui.Port.setText(button._associated_ssh_host['Port'])
		ui.IdentityFile.setText(button._associated_ssh_host['IdentityFile'])

		if editHost.exec_():
			button._associated_ssh_host['Host'] = str(ui.Name.text())
			button._associated_ssh_host['HostName'] = str(ui.HostName.text())
			button._associated_ssh_host['User'] = str(ui.User.text())
			button._associated_ssh_host['Port'] = str(ui.Port.text())
			button._associated_ssh_host['IdentityFile'] = str(ui.IdentityFile.text())
			button.setText(button._associated_ssh_host['Host'])
		self.ssh_config.save()
		print "Clicked edit button"

	def on_removeButton_clicked(self, b):
		print "Clicked remove button"

		button = self.get_checkedButton()

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

