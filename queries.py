def searchUserName(userName):
    return "SELECT * FROM Users WHERE userName = '" + userName + "';"


def getPassword(userName):
    return "SELECT passWord FROM Users WHERE userName = '" + userName + "';"


def getHotelsByCity(city):
    return "SELECT * FROM Hotels WHERE city = '" + city + "';"


def getHotelsByState(state):
    return "SELECT * FROM Hotels WHERE state = '" + state + "';"


def insertAccount(firstName, lastName, userName, passWord, cardNum, address):
    return "INSERT INTO Users (firstName, lastName, userName, passWord, cardNum, address) \n" \
           "VALUES	('" + firstName +"', '"+ lastName + "', '" + userName +"', '" + passWord + "', '" + cardNum + "', '" + address + "');"