#!/usr/bin/env python

from settings import *
from imaplib import *
from emailprocessor import *

proc = EmailProcessor()
proc.open(LOCAL_INBOX_SERVER, 
	LOCAL_INBOX_PORT, LOCAL_INBOX_USER, LOCAL_INBOX_PASSWORD)

if proc.hasMessages():
	email = proc.pollNextMessage()
	print email['From']

proc.close()
