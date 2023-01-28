
#---------------------------------------------------------------------------------
# >>>>> Steps to folow while programming :-

# Step 1  Understand the problem statement
# Step 2  Write the algorithm
# Step 3  Decide the programming language
# Step 4  Write the program
# Step 5  Test the program
#---------------------------------------------------------------------------------



#---------------------------------------------------------------------------------
# ------------------ Process Log with Periodic Mail Sending Facility ----------------------

    # Please follow below rules while designing automation script as : 
            # Accept input through command line or through file.
            # Display any message in log file instead of console.
            # For robustness handle every expected exception.
            # Perform validations before taking any action. 
            # Create user defined modules to store the functionality.
#---------------------------------------------------------------------------------

# Design automation script which performs following task.

# Accept Directory name from user and delete all duplicate files from the specified directory by considering the checksum of files.
# Create one Directory named as Vikas and inside that directory create log file which maintains all names of duplicate files which are deleted.
# Name of that log file should conatains the date and time at which that file gets created.
# Accept duration in minutes from user and perform task of duplicate file removal after the specific time interval.
# Accept Mail id from user and send the attachment of the log file.
# Mail body should contains statistics about the operation of duplicate file removal.
# Mail body should contains below things:
        # Starting time of scanning
        # Total number of files scanned
        # Total number of duplicate files found.

# Consider below command line options for the gives script.

#### DuplicateFileRemoval.py  E:/Data/Demo 50 abc@gmail.com

# - DuplicateFileRemoval.py
        # Name of python automation script

# - E:/Data/Demo
        # Absolute path of directory which may contains duplicate files.

# - 50
        # Time interval of script in minutes

# - abc@gmail.com
        # Mail ID of the receiver

#---------------------------------------------------------------------------------

import os
import time
import psutil
import urllib2
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#---------------------------------------------------------------------------------
# Function Name : is_connected
# Description : URL Open
# Author : Bade Vikas Vasudeo
# Date : 15/09/2022
#---------------------------------------------------------------------------------

def is_connected():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

#---------------------------------------------------------------------------------
# Function Name : MailSender
# Description : Sending the mail with attached file
# Author : Bade Vikas Vasudeo
# Date : 15/09/2022
#---------------------------------------------------------------------------------

def MailSender(filename, time):
    try:
        fromaddr = "neomio.enterprises@gmail.com"
        toaddr = "shivconstruction0102@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr

        msg['To'] = toaddr

        # Body of the Email
        body = """
        Hello %s
        Welcome to Neomio Enterprises.
        Please find attached document which contains Log of Running Process.
        Log file is created at : %s

        This is auto gennerated mail.

        Thanks & Regards,
        Bade Vikas
        Neomio Enterprises
            """ % (toaddr, time)

        # Subject of the Email
        Subject = """
        Neomio Enterprises Process log generated at : %s
            """ % (time)
        
        msg['Subject'] = Subject

        # Attachment of File
        msg.attach(MIMEText(body, 'plain'))

        # Attachment File is Open
        attachment = open(filename, "rb")

        p = MIMEBase('application', 'octet-stream')

        # Load and Read the file
        p.set_payload((attachment).read)

        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename = %s" % filename)

        msg.attach(p)

        s = smtplib.SMTP('neomio.enterprises@gmail.com', 587)

        s.starttls()

        # password of Email
        s.login(fromaddr, "Vikas@1998")

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit()

        print("Log file successfully sent through Mail")

    except Exception as E:
        print("Unable to send main.",E)

#---------------------------------------------------------------------------------
# Function Name : ProcessLog
# Description : Process Log file should contains the date and time
# Author : Bade Vikas Vasudeo
# Date : 15/09/2022
#---------------------------------------------------------------------------------

def ProcessLog(log_dir = 'Neomio'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "_" * 80
    log_path = os.path.join(log_dir, "NeomioLog%s.log" % (time.ctime()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Neomio Enterprises Process Logger : "+time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    for element in listprocess:
        f.write("%s\n" % element)

    print("Log file is successfully generated at location %s" % (log_path))

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender(log_path, time.ctime())
        endTime = time.time()

        print('Took %s seconds to send main' % (endTime - startTime))
    else:
            print("There is no internet connection")

#---------------------------------------------------------------------------------
# Function Name : main
# Description : main function from where execution starts
# Author : Bade Vikas Vasudeo
# Date : 15/09/2022
#---------------------------------------------------------------------------------

def main():
    print("--------------------------- By Bade Vikas -----------------------------")

    print("----- Application name : Periodic Process Logger with Auto Scheduled Log Report Facility -----")
    print("--------------------------- File Name : "+argv[0]+" ---------------------------")

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used log record of running processess")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error : Invalid Datatype of Input")

    except Exception as E:
        print("Error : Invalid Input", E)

#---------------------------------------------------------------------------------
    # Application Starter
#---------------------------------------------------------------------------------

if __name__ == "__main__":
    main()