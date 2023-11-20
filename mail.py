import smtplib
my_email = 'folashadebewaji@gmail.com'
password = 'Folashade540'
 
connection = smtplib.SMTP(port=53, source_address= 'smtp.gmail.com')
connection.starttls()
connection.login = (my_email,password)
connection.sendmail(from_addr=my_email, to_addrs= 'gracebolu@gmail.com', msg= 'Enroll for your trading signal at #20,000 and enjoy December dollar cashout with lunchaeXchange')
connection.close()

# GENERATION OF QRCODE

import pyqrcode

# import png
q = pyqrcode.QRCode(error='could not be resolved', version= 3)
q.add()
Registration_link = 'https://wa.me/c/2349090397455'
url = pyqrcode.create(Registration_link)


