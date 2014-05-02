#!/usr/bin/python
import os

class SSH_Config:
	@staticmethod
	def open_or_create_file(file):
		directory = os.path.dirname(file)
		if not os.path.exists(directory):
			os.makedirs(directory)
		try:
			return open(file, "rw")
		except:
			return open(file, "w+")

	@staticmethod
	def split_ssh_config_content(ssh_config_content):
		hosts = list()
		host = None
		for param in ssh_config_content:
			try:
				(key, value) = param.split()
				if not host:
					host = {key: value}
				elif key not in ("Host", "Match"):
					host[key] = value
				else:
					hosts.append(host)
					host = None
			except:
				if host:
					hosts.append(host)
					host = None
		hosts.append(host)

		return hosts

	def __init__(self, file="~/.ssh/config"):
		self.fd = self.open_or_create_file(file)
		ssh_config_content = map(str.strip, self.fd.readlines())
		self.hosts = self.split_ssh_config_content(ssh_config_content)
	
	def __str__(self):
		return str(self.hosts)

if __name__ == '__main__':
	test_config = SSH_Config('./ssh_config')
	print test_config
