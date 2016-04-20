from datetime import date

def isValidPhone(tPhone):
	validity = False
	# check if '(###)###-####'
	if len(tPhone)==13 and tPhone[0]=='(' and tPhone[4]==')' and tPhone[8]=='-':
		if tPhone[1:4].isdigit() and tPhone[5:8].isdigit() and tPhone[9:].isdigit():
			validity = True
	# check if '###-###-####'
	elif len(tPhone)==12 and tPhone[3]==tPhone[7]=='-':
		if tPhone[:3].isdigit() and tPhone[4:7].isdigit() and tPhone[8:].isdigit():
			validity = True
	return validity


class Text:
	def __init__(self, tmpPhoneStr, tmpArrivaleDate, tmpMsgTxt):
		self._phoneNum = tmpPhoneStr
		self._date = tmpArrivaleDate
		self._msg = tmpMsgTxt
		self.setRead(False)

	def setRead(self, tmpIfRead):
		self._isRead = tmpIfRead
		
	def toList(self):
		return [self.getPhone(), self.getDate(), self.getMsg()]
	
	def getPhone(self):
		return self._phoneNum

	def getDate(self):
		return self._date

	def getMsg(self):
		return self._msg

	def isUnread(self):
	    return not self._isRead

	def readMsg(self):
	    self.setRead(True)
	    return self._msg

	

class SMSInbox:
	def __init__(self):
		self._messages=[]

	def printOneMessage(self, tmpIndex):
		print((self.getInbox()[tmpIndex]).toList())

	def addNewArrival(self, tmpPhoneStr, tmpArrivalDate, tmpMsgStr):
		# returns True if successfully put inbox
		# check if valid phone number
		if isValidPhone(tmpPhoneStr) and len(tmpMsgStr)<=140:
			self._messages.append(Text(tmpPhoneStr, tmpArrivalDate, tmpMsgStr))
			return True
		else:
			return False
	
	def countMessages(self):
		# returns num messages in inbox
		return len(self._messages)
	
	def deleteMsg(self, tIndex):
		deleted = -1
		# returns 1 if message is deleted, or -1 if not
		if tIndex.isdigit() and int(tIndex) < len(self.getInbox()):
			self._messages.pop(int(tIndex))
			deleted = 1
		return deleted

	def deleteAllMsgsFromSender(self, tmpPhoneStr):
		# returns number of messages deleted
		tmpNewInbox= []
		countDeleted = len(self.getInbox())
		for text in self.getInbox():
			if text.getPhone() != tmpPhoneStr:
				tmpNewInbox.append(text)
				countDeleted -= 1
		self._messages = tmpNewInbox
		return countDeleted

	def deleteOlderMsgs(self, numDays):
		# returns number of messages deleted
		tmpNewInbox = []
		countDeleted = len(self.getInbox())
		# check that the number of days is valid
		if numDays < 0:
			return -1
		for text in self.getInbox():
			if (date.today() - text.getDate()).days >= numDays:
				tmpNewInbox.append(text)
				countDeleted -= 1
		self._messages = tmpNewInbox
		return countDeleted
	
	def retrieveUnread(self):
		# returns list of list of phoneNumber List
		tmpNewInbox = []
		for text in self.getInbox():
			if text.isUnread():
			    tmpNewInbox.append(text.getMsg())
		return tmpNewInbox
	
	def retrieveMsgFromPhone(self, tmpPhoneStr):
	    # returns list of phoneNumber lists
	    # check that phoneNumber is valid
		if not isValidPhone(tmpPhoneStr):
		    return []
		# otherwise get list of messages by phone numbers
		tmpInbox = []
		for text in self.getInbox():
		    if text.getPhone() == tmpPhoneStr:
		        # change text to read
		        text.readMsg()
		        tmpInbox.append(text.toList())
		return tmpInbox
	
	def retrieveMsgsAfterDate(self, tmpDate):
		# return list of phoneNumber Lists
		tmpInbox = []
		# check that the number of days is valid
		for text in self.getInbox():
		    if text.getDate() > tmpDate:
		        # change text to read
		        text.readMsg()
		        tmpInbox.append(text.toList())
		return tmpInbox
	
	def clearInbox(self):
		self._messages=[]
	
	def getInbox(self):
		return self._messages

	def __str__(self):
	    tmpStr="{:20s}{:20s}{:12s}{:<140s}".format("SenderPhone", "Date/Time Recieved", "Read?", "Message")
	    for text in self.getInbox():
	        read = "Yes"
	        if text.isUnread:
	            read = "No"
	        tmpStr+="\n{:20s}{:20s}{:12s}{:<140s}".format(text.getPhone(), \
	        text.getDate().strftime('%m/%d/%Y'), read, text.getMsg())
	    return tmpStr

def printMenu(tMessages):
    print("\n\nMENU\n")
    ct = 0
    for oneMessage in tMessages:
        ct += 1
        print(str(ct) + '. ' + oneMessage)
        
def isValidDate(string):
    if len(string)==10 and string[2]==string[5]=="/" and string[:2].isdigit() and int(string[:2])<=12\
    and string[3:5].isdigit() and int(string[3:5])<=31 and string[6:].isdigit() and int(string[6:])>0:
        return True
    return False

MENU_OPTIONS = ("Add New Message", "Count of messages", "Print Inbox",\
                "Print individual message", "Retrieve list of unread messages",\
                "Retrieve all messages from a particular phone number", \
                "Retrieve all messages arrived after a date/time",\
                "Delete individual message", "Delete all messages from a particular sender",\
                "Delete all messages older than # of days", "Clear Inbox", "Quit")

inbox = SMSInbox()
# temporary
inbox.addNewArrival("123-123-1234", date(2016, 4, 19), "message1")
inbox.addNewArrival("000-000-0000", date(2015, 11, 8), "message2")
inbox.addNewArrival("123-123-1234", date(2015, 11, 9), "message3")
printMenu(MENU_OPTIONS)
choice = input('\nPlease enter your choice... ')
while choice != str(len(MENU_OPTIONS)):
    if choice == "1":
        # ask for input and then enter new message into inbox
        tmpPhone = input("Please enter a phone number to send the text from: ")
        if not isValidPhone(tmpPhone):
            tmpPhone = input("Bad Input -- Please enter a phone number to send the text from: ")
        tmpDate = input("Please enter a date (MM/DD/YYYY) in which the  text was recieved: ")
        if not isValidDate(tmpDate):
            tmpDate = input("Bad Input -- Please enter a date (MM/DD/YYYY) in which the  text was recieved: ")
        tmpDate = date(int(tmpDate[6:]), int(tmpDate[:2]), int(tmpDate[3:5]))
        tmpMsg = input("Please enter a message to send")
        inbox.addNewArrival(tmpPhone, tmpDate, tmpMsg)
    
    elif choice == "2":
        # print count of messages
        print('\nCount of Messages:', inbox.countMessages(),"\n\n")
        input("Please press enter to continue")
		
    elif choice == "3":
        # print all messages
        print(inbox)
		
    elif choice == "4":
        # get individual message
        print("\n\nPlease enter an integer for which message you would like to print from 0 up to", end=" ") 
        tmpIndex = input(inbox.countMessages()-1)
        if tmpIndex.isdigit():
            tmpIndex = int(tmpIndex)
        while tmpIndex not in range(inbox.countMessages()):
            print("\n\Error -- 0 up to", end=" ")
            tmpIndex = input(inbox.countMessages()-1)
            if tmpIndex.isdigit():
                 tmpIndex = int(tmpIndex)
        inbox.printOneMessage(tmpIndex)
	
    elif choice == "5":
        # get unread messages from phone
        if (len(inbox.retrieveUnread()) == 0):
            print("No Unread messages")
        else:
            for message in inbox.retrieveUnread():
                print(message)
		
    elif choice == "6":
        # get messages from phone
        tmpPhone = input("Please enter a phone number to see texts: ")
        if not isValidPhone(tmpPhone):
            tmpPhone = input("Bad Input -- Please enter a phone number to send the text from: ")
        print(inbox.retrieveMsgFromPhone(tmpPhone))
		
    elif choice == "7":
        # get all messages after a date
	    tmpDate = input("Please enter a date (MM/DD/YYYY) in which the  text was recieved: ")
	    if not isValidDate(tmpDate):
	        tmpDate = input("Bad Input -- Please enter a date (MM/DD/YYYY) in which the  text was recieved: ")
	    print(tmpDate[:2], tmpDate[3:5],tmpDate[-4:])
	    tmpDate= date(int(tmpDate[-4:]),int(tmpDate[:2]),int(tmpDate[3:5]))
	    print(inbox.retrieveMsgsAfterDate(tmpDate))
		
    elif choice == "8":
        # delete a message based on index
	    print(inbox)
	    print("\nPlease enter the index of the message you would like to delete from 0 to", end=" ")
	    tmpIndex = input(inbox.countMessages()-1)
	    inbox.deleteMsg(tmpIndex)
		
    elif choice == "9":
        # delete all messages from a sender
	    print(inbox)
	    tmpPhone = input("Please enter a phone number to delete all messages from: ")
	    if not isValidPhone(tmpPhone):
	        tmpPhone = input("Bad Input -- Please enter a phone number to delete all messages from: ")
	    print(inbox.deleteAllMsgsFromSender(tmpPhone), "messages deleted")
        
	
    elif choice == "10":
	    print(inbox)
	    tmpDays = input("Please enter the number of days: ")
	    if not tmpDays.isdigit():
	        tmpDays = input("Bad Input -- Please enter the number of days old: ")
	    
	    print(inbox.deleteOlderMsgs(int(tmpDays)), "messages deleted")
		
    elif choice == "11":
        inbox.clearInbox()
        
    else:
        print("Bad Input!")
    
    printMenu(MENU_OPTIONS)
    choice = input('\nPlease enter your choice: ')
	

