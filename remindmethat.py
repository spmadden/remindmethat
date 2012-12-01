#!/usr/bin/env python

from settings import *
from imaplib import *
from emailprocessor import *
from time import sleep

proc = EmailProcessor()
proc.open(LOCAL_INBOX_SERVER, 
	LOCAL_INBOX_PORT, LOCAL_INBOX_USER, LOCAL_INBOX_PASSWORD)
send = EmailSender()
send.open(LOCAL_SMTP_SERVER,
	LOCAL_SMTP_PORT, LOCAL_INBOX_USER, LOCAL_INBOX_PASSWORD)

while True:
	if not proc.hasMessages():
		print "sleeping"
		sleep(10)
		continue
	email = proc.pollNextMessage()
	oldfrom = email['From']
	contains = True in [allowed in oldfrom for allowed in ACCEPTED_EMAILS_LIST]
	print contains

	newEmail = message.Message()
	newEmail.set_payload(email.get_payload(0,True))

	newEmail['From'] = LOCAL_INBOX_USER
	newEmail['To'] = RTM_INBOX_EMAIL
	newEmail['Subject'] = email['Subject']
	if contains:
		send.send(newEmail)

send.close()
proc.close()
