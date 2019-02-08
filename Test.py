from datetime import date, datetime
import json
# import excelwriter
import logging
import sys, os
# import sendemail
import utilities

# a = datetime.date
# d = datetime.weekday
# d = datetime.year

# d = datetime.today()
# print(d)
# print(d.today())
# print(d.weekday())
# print(d.year)
# print(d.month)
# print(d.day)
# print(d.dst())
# print(d.hour)
# print(d.minute)
# print(d.second)
# print(d.date())

# newDate = datetime(datetime.today().year,datetime.today().month,datetime.today().day)
# print(newDate)


# print("datetime.today():{0}".format(datetime.today()))
# print("datetime.date:{0}".format(datetime.date))

# Converting date into DD-MM-YYYY format. print(d. strftime('%d-%m-%Y'))

# Load Configurations
# with open('config.json') as config_json_data_file:
#     configData = json.load(config_json_data_file)   


# payload = json.dumps(configData)

# hostname = "machineA.host.com"
# print(hostname)
# print(configData)
# print(payload)
# print(payload1)

# Test Excel Writer Utility
oneDimensionalHeaderList = ["Name","Gender","Age"]
twoDimensionalDataList = [["Jai","Male",40],["Geetu","Female",36],["Jia","Female",10],["Sudhir","Male",40]]
utilities.excelwriter.generate_Excel("SampleExcelFile.xls","Data",oneDimensionalHeaderList,twoDimensionalDataList)

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# print(sys.path)
# sys.path.append("/Users/jchenchl/OneDrive - JC Penney/Tools/Utilities")
# print(sys.path)
# import send_email

# Test Utility send_email
emailSMTPHost = "mail.jcpenney.com"
emailSMTPPort = 25
# emailSubject = "Test Utility send_email"
emailSubject = str(oneDimensionalHeaderList)
emailFrom = "jchenchl@jcp.com"
emailTo = "jchenchl@jcp.com"
emailCC = "jchenchl@jcp.com"
# emailBody = "This is email body."
emailBody = str(twoDimensionalDataList)

utilities.sendemail.send_email(emailSMTPHost,emailSMTPPort,emailSubject, emailFrom, emailTo, emailCC, emailBody)

