#!/usr/local/bin/python

import sys
import socket
import smartsheet

Token="<smartsheet token>"

smartsheet = smartsheet.Smartsheet(Token)

sshKeyColumn = 4
hostColumn = 3
userColumn = 2
sheetName = "Sshlogin"
sheetId = <sheetid>
hostname = socket.gethostname()

# Search is crap as it just tell you the row something occurs in not the column
# infact the api for smart sheets is pretty shit to be honest 
#results = smartsheet.Search.search_sheet(sheetId,sys.argv[1])

# Get a whole column as it easier to do the search in pythnon than on the api 
sheet = smartsheet.Sheets.get_sheet(sheetId)
for row in sheet.rows:
	if row.cells[userColumn].value == sys.argv[1]:
		if row.cells[hostColumn].value == hostname:
			print row.cells[sshKeyColumn].value




