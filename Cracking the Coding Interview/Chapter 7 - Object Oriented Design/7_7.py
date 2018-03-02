"""
7.7 Chat Server
Explain how you would design a chat server. In particular, provide details
about the various backend components, classes, and methods. What would be
the hardest problems to solve?
"""

class Room:
    Room.__allRooms = []
    def __init__(self, name='', users):
        """
        input
            name: name of room (string)
            users: users in the room (list of User)
        output
            None
        """
        self.__name = name
        self.__users = users
        self.__messages = [] # dictionary of user and messages
        Room.__allRooms.append(self)

    def addUser(self, user):
        self.__users.append(user)

    def getUsers(self):
        return self.__users

    def removeUser(self, user):
        self.__user = [x for x in self.__users if user!=x]

    def addMsg(self, msg, user):
        self.__messages.append({user: msg})

    def getMsgs(self):
        return self.__messages

    def removeMsg(self, someMsg):
        self.__messages = [x for x in self.__messages if someMsg != x]

    def updateName(self, newName):
        self.__name = newName

    # class-level method
    def findRoom(users):
        # see if one room has same users
        boolRooms = [set(room.getUsers()) == set(users) for room in Room.__allRooms]
        if any(boolRooms):
            # get index of Room
            index = [i for i, x in enumerate(boolRooms) if x==True].pop()
            return Room.__allRooms[index]
        return -1 # if not found


class User:
    def __init__(self, name):
        self.__name = name
        self.__isOnline = True

    def signOut(self):
        self.__isOnline = False

    def signIn(self):
        self.__isOnline = True

    def sendMessage(self, users, msg):
        """expect users to be a list of users to send the message to"""
        room = Room.findRoom(users.append(self))
        # if room doesn't exist, create a room and add the message to the room
        if room == -1:
            room = Room(",".join(users), users.append(self))
        room.addMsg(msg, self)

class Message:
    def __init__(self, text):
        self.__text = text

    def getText(self):
        return self.__text
