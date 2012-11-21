from imaplib import *
from email import *
from smtplib import *

class EmailException(Exception):
	def __init__(self, message):
		self.value = message

	def __str__(self):
		return repr(self.value)
	

class EmailProcessor:

	def __init__(self):
		self.imapi = None

	def open(self, server, port, user, passwd):
		if self.imapi != None:
			raise EmailException("Already initialized!")
		self.imapi = IMAP4_SSL(server, port)
		try:
			self.imapi.login(user, passwd)
		except Exception:
			raise EmailException
		
		self.imapi.select()

	def hasMessages(self):
		if self.imapi == None:
			raise EmailException("Did you forget to Open() me?")
		typ, data = self.imapi.search(None, 'ALL')
		self.nums = data[0].split()
		return len(self.nums) > 0

	def pollNextMessage(self):
		if len(self.nums) == 0:
			raise EmailException("No messages in the queue!")
		num = self.nums.pop(0)
		typ2, data2 = self.imapi.fetch(num, '(RFC822)')
		body = data2[0][1]
		self.imapi.store(num, '+FLAGS', '\\Deleted')
		self.imapi.expunge()
		return message_from_string(body)

	def close(self):
		self.imapi.close()

class EmailSender:
	def __init__(self):
		pass

	def open(self, server, port, user, passwd):
		pass

	def send(self, email):
		pass

