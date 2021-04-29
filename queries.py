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
           "VALUES ('" + firstName +"', '"+ lastName + "', '" + userName +"', '" + passWord + "', '" + cardNum + "', '" + address + "');"


def insertHotel(name, city, state, address):
    return "INSERT INTO Hotels(name, city, state, address)\n" \
           "VALUES ('" + name + "', '" + city + "', '" + state + "', '" + address + "');"


def resetDB():
    return """DROP TABLE IF EXISTS Rooms;
DROP TABLE IF EXISTS Hotels;
DROP TABLE IF EXISTS Cars;
DROP TABLE IF EXISTS Dealerships;
DROP TABLE IF EXISTS Users;


CREATE TABLE Hotels (
    hotelID   INTEGER,
    name      TEXT NOT NULL,
    city      TEXT NOT NULL,
    state     TEXT NOT NULL,
    address   TEXT NOT NULL,
    PRIMARY KEY(hotelID)
);

CREATE TABLE Rooms (
    roomID    INTEGER,
    hotelID   INTEGER,
    num       INTEGER NOT NULL,
    reserved  INTEGER NOT NULL,
    capacity  INTEGER NOT NULL,
    rate      REAL,
    PRIMARY KEY(roomID),
    FOREIGN KEY(hotelID) REFERENCES Hotels(hotelID)
);

CREATE TABLE Dealerships (
    dealerID    INTEGER,
    name        TEXT NOT NULL,
    city        TEXT NOT NULL,
    state       TEXT NOT NULL,
    address     TEXT NOT NULL,
    PRIMARY KEY(dealerID)
);                                          

CREATE TABLE Cars (
    carID     INTEGER,
    dealerID  INTEGER,
    reserved  INTEGER NOT NULL,
    make      TEXT NOT NULL,
    model     TEXT NOT NULL,
    body      TEXT NOT NULL,
    rate      REAL,
    PRIMARY KEY(carID),
    FOREIGN KEY(dealerID) REFERENCES Dealerships(dealerID)
);

CREATE TABLE Users (
    userID    INTEGER,
    firstName TEXT NOT NULL,
    lastName  TEXT NOT NULL,
    userName  TEXT NOT NULL UNIQUE,
    passWord  TEXT NOT NULL,
    cardNum   TEXT,
    address   TEXT NOT NULL,
    PRIMARY KEY(userID)
);
"""