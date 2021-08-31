import imaplib, struct, time, email

class Mail():
    def __init__(self):
        self.user= 'hoangviet2373@gmail.com'
        self.password= 'Viet123hp'
        #self.ser = serial.Serial('/dev/tty.usbmodem621', 9600)
        self.M = imaplib.IMAP4_SSL('imap.gmail.com', '993')
        self.M.login(self.user, self.password)
        
    def checkMail(self):
        self.M.select('Inbox')
        self.unRead = self.M.search(None, 'UnSeen')
        return len(self.unRead[1][0].split())
    
    def getContent(self):
        typ, data = self.unRead
        for num in data[0].split():
            typ, data = self.M.fetch(num, '(RFC822)')
            print('Message %s\n%s\n' % (num, data[0][1]))
        
Email = Mail()

# check for new mail every minute
while True:
    # print ('Sending')
    count = Email.checkMail()
    content = Email.getContent()
    if count > 0:
        print (count)
        print (content)
        print ("co email moi")
    elif count == 0:
        print ("khong co email moi")
    time.sleep(3)