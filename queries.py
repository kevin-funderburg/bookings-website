def searchUserName(userName):
    return "SELECT * FROM Users WHERE userName = '" + userName + "';"


def getPassword(userName):
    return "SELECT passWord FROM Users WHERE userName = '" + userName + "';"


def getHotelsByCity(city):
    return "SELECT * FROM Hotels WHERE city = '" + city + "';"


def getHotelsByState(state):
    return "SELECT * FROM Hotels WHERE state = '" + state + "';"


def getUserID(att, val):
    return "SELECT userID FROM Users WHERE " + att + " = '" + val + "';"


def updateAccount(id, att, newVal):
    return "UPDATE Users\n" \
           "SET " + att + " = '" + newVal + "'\n" \
           "WHERE userID = " + str(id) + ";"

def insertAccount(firstName, lastName, userName, passWord, cardNum, address):
    return "INSERT INTO Users (firstName, lastName, userName, passWord, cardNum, address) \n" \
           "VALUES	('" + firstName +"', '"+ lastName + "', '" + userName +"', '" + passWord + "', '" + cardNum + "', '" + address + "');"