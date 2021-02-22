#!/bin/python3

#pip install twilio
import os, sys
from twilio.rest import Client

#Twilio account information
accountSID = 'ENTER SID HERE'
authToken = 'ENTER TOKEN HERE'

#Authorize with Twilio and send the message
def textmyself(message):
        client = Client(accountSID, authToken)
        client.api.account.messages.create(to="ENTER PHONE NUMBER TO SEND TO", from_="ENTER TWILIO NUMBER HERE", body=message)

#Run the Nmap scan then send a text message.
try:
        os.system('nmap -A -p- -T4 ' + str(sys.argv[1]) + ' -o nmap_' + str(sys.argv[1]) + '.txt')
        textmyself('Your nmap scan of IP ' + str(sys.argv[1]) + ' is complete')
except:
        print ('Usage: ./Nmap_Scan_Notifier.py 10.10.10.10')
        sys.exit()
