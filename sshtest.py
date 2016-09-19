#!/usr/bin/python

import gspread
import sys
import socket
from oauth2client.service_account import ServiceAccountCredentials
import logging
import logging.handlers

logger = logging.getLogger('sshauthGsheet')
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address = '/dev/log')
logger.addHandler(handler)

# Change this to the API ID you get
jsonData = { "type": "service_account", "project_id": "sshaut", "private_key_id": "3", "private_key": "-----BEGIN PRIVATE KEY-----\n\n-----END PRIVATE KEY-----\n", "client_email": "test@ssh.gserviceaccount.com", "client_id": "127", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://accounts.google.com/o/oauth2/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test%40ssh.iam.gserviceaccount.com" }

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_dict(jsonData,scope)
# Or if you dont want to inline the auth which means you could keep the details more secret
#credentials = ServiceAccountCredentials.from_json_keyfile_name('/etc/config/sshauth.json',scope)


# Setting that define sheet and which column to use for what
sshKeyColumn = 4
hostColumn = 3
userColumn = 2
sheetName = "SSHauth"
hostname = socket.gethostname()

gc = gspread.authorize(credentials)
worksheet = gc.open(sheetName).sheet1

cellList = worksheet.findall(sys.argv[1])

logger.critical('Mached %d with user "%s" testing for  host "%s"',len(cellList),sys.argv[1],hostname)


for cell in cellList:
  if cell.col == userColumn:
	if hostname == worksheet.cell(cell.row,hostColumn).value:
                # XXX insert cacheing here 
  		print worksheet.cell(cell.row,sshKeyColumn).value
