# fill in your username and password to send emails!
import smtplib
import random
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def secret_santa(names):
    copy_names = names[:]
    random.shuffle(copy_names)
    assignments = {}

    # prevents cycles by randomly permuting list, and
    # assigning each person the person to their right
    for i in range(len(copy_names)):
        giver = copy_names[i]
        taker = copy_names[(i + 1) % len(copy_names)]
        assignments[giver] = taker
    return assignments

def string_to_list(string):
    current = string
    name = ''
    res = []
    while len(current) > 0:
        pop = current[0]
        if pop != ',':
            name += pop
        else:
            res.append(name)
            name = ''
            current = current [1:]
        current = current[1:]
    res.append(name)
    return res

#print emails
  
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
  
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()


def email(emails, res, price, msg):
    
    for name in res:
        sendemail(from_addr    = 'XXXXXXXXXX@gmail.com', 
                  to_addr_list = [emails[name]],
                  cc_addr_list = [''], 
                  subject      = 'Secret Santa :D', 
                  message      = 'Herrrooo ' + name + "!\n\nYour secret santa is " + res[name] +"! \
The spending limit is $" + price + "--be creative and have fun! " + msg + "\n\nRUV YOUUUU,\nSecret Santa Generator\n\n\
But actually, I'm a Python robot... ;)", 
                  login        = 'XXXXXXXXXXXXX', 
                  password     = 'XXXXXXXXXXXXX')



def run_secret_santa_with_kerb(namestring, kerberosstring):
    names = string_to_list(namestring)
    res = secret_santa(names)

    true = None
    while true not in ['yes', 'no']:
        true = raw_input('Do you want to send emails? Reply yes or no. ')
    if true == 'yes':
        true = True
    else:
        true = False
    if not true:
        ask = None
        while ask not in ['yes', 'no']:
            ask = raw_input('Do you want to see the results? Reply yes or no. ')
        if ask == 'yes':
            return res
        else:
            return 'Okay then...'
    else:
        kerbs = string_to_list(kerberosstring)
        emails = dict()
        for i in range(len(names)):
            emails[names[i]] = kerbs[i] + '@mit.edu'
        price = raw_input('What price range do you want to set? (i.e. 15-20) ')
        msg = raw_input('Write a special message to send to everyone: ')
        return email(emails, res, price, msg)


def email_secret_santa(names, res, emaillist):
    price = raw_input('What price range do you want to set? (i.e. 15-20) ')
    msg = raw_input('Write a special message to send to everyone: ')
    return email(emails, res, price, msg)

def return_res(res):
    return res

def run_secret_santa(namestring, emailstring):
    names = string_to_list(namestring)
    res = secret_santa(names)
    emaillist = string_to_list(emailstring)
    emails = dict()
    for i in range(len(names)):
        emails[names[i]] = emaillist[i]

    true = None
    while true not in ['yes', 'no']:
        true = raw_input('Do you want to send emails? Reply yes or no. ')
    if true == 'yes':
        email_secret_santa(names, res, emaillist)

    ask = None
    while ask not in ['yes', 'no']:
        ask = raw_input('Do you want to see the results? Reply yes or no. ')
    if ask == 'yes':
        return return_res(res)

    save = None
    while save not in ['yes', 'no']:
        save = raw_input('Do you want to save the results? Reply yes or no. ')    
    if save == 'yes':
        print 'hi'
