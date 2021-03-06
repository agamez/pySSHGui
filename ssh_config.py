#!/usr/bin/python
import os

class SSH_Config:
	@staticmethod
	def split_ssh_config_content(ssh_config_content):
		hosts = list()
		empty_host = {'User' : 'user', 'Port' : '22', 'IdentityFile' : '~/.ssh/id_rsa'}
		host = empty_host.copy()
		for param in ssh_config_content:
			try:
				(key, value) = param.split()
				if not 'Host' in host:
					host[key] = value
				elif key not in ("Host", "Match"):
					host[key] = value
				else:
					hosts.append(host)
					host = empty_host.copy()
			except:
				if 'Host' in host:
					hosts.append(host)
					host = empty_host.copy()
		if 'Host' in host:
			hosts.append(host)

		return hosts

	def save(self):
		directory = os.path.dirname(self.file)
		if not os.path.exists(directory):
			os.makedirs(directory)

		fd = open(os.path.expanduser(self.file), "w")
		for host in self.hosts:
			copied_host = host.copy()
			fd.write("Host %s\n" % copied_host["Host"])
			del(copied_host["Host"])
			for key in copied_host:
				fd.write("\t%s %s\n" % (key, copied_host[key]))
			fd.write("\n")
		fd.close()

	def __init__(self, file="~/.ssh/config"):
		self.file=os.path.expanduser(file)
		try:
			fd = open(self.file, "rw")
			file_contents = fd.readlines()
			fd.close
		except:
			file_contents=None

		ssh_config_content = map(str.strip, file_contents)
		self.hosts = self.split_ssh_config_content(ssh_config_content)

	def __str__(self):
		return str(self.hosts)

if __name__ == '__main__':
	test_config = SSH_Config('./ssh_config')
	print test_config
