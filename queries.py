def searchUserName(userName):
    return "SELECT * FROM Users WHERE userName = '" + userName + "';"


def getPassword(userName):
    return "SELECT passWord FROM Users WHERE userName = '" + userName + "';"


def getHotelsByCity(city, state):
    return "SELECT * FROM Hotels WHERE city = '" + city + "' and state = '" + state + "';"


def getHotelsByState(state):
    return "SELECT * FROM Hotels WHERE state = '" + state + "';"


def getUserID(att, val):
    return "SELECT userID FROM Users WHERE " + att + " = '" + val + "';"


def getHotelID(name, city):
    return "SELECT hotelID FROM Hotels WHERE name = '" + name + "' and city = '" + city + "';"


def updateHotel(id, att, newVal):
    return "UPDATE Hotels\n" \
           "SET " + att + " = '" + newVal + "'\n" \
           "WHERE hotelID = " + str(id) + ";"


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


def populateDB():
    return """INSERT INTO Hotels (name, city, state, address)
VALUES ('Ambassador', 'Austin', 'Texas', '72 Amy Street'),
       ('Marriot', 'New York', 'New York', '75 West 85th Street'),
       ('Best Western', 'San Antonio', 'Texas', '812 Winding Brook'),
       ('Alpine Inn', 'Seattle', 'Washington', '637 Real Street'),
       ('Gold Country', 'San Francisco', 'California', '718 Fake Street'),
       ('Route 78', 'Portland', 'Oregon', '11 Route 78'),
       ('Claw Inn', 'Houston', 'Texas', '661 Hopping Frog'),
       ('Dockyard Place', 'Chicago', 'Illinois', '817 Silly Spaceman'),
       ('Kate''s Place', 'San Diego', 'California', '85 85th Street');


INSERT INTO Rooms (hotelID, num, reserved, capacity, rate)
VALUES  (5, 102, 1, 2, 99.00),
        (4, 301, 0, 2, 199.00),
        (5, 201, 0, 3, 45.00),
        (6, 104, 0, 2, 89.00),
        (6, 202, 0, 4, 25.00),
        (7, 103, 1, 2, 150.00),
        (7, 202, 1, 4, 100.00),
        (8, 301, 0, 3, 200.00),
        (8, 204, 0, 2, 199.99),
        (9, 101, 0, 3, 85.00),
        (9, 204, 1, 2, 55.00),
        (1, 103, 1, 2, 88.00),
        (2, 201, 0, 2, 75.00),
        (2, 101, 0, 4, 135.00),
        (1, 250, 1, 2, 87.00),
        (3, 300, 0, 4, 300.00),
        (4, 500, 0, 2, 125.00);


INSERT INTO Dealerships (name, city, state, address)
VALUES  ('First Texas Honda', 'Austin', 'Texas', '728 George Street'),
        ('Toyota of Austin', 'Austin', 'Texas', '23 Salmon Lane'),
        ('Tesla', 'New York', 'New York', '838 Led Zeppelin Drive'),
        ('Classic Chevrolet', 'San Francisco', 'California', '910 Big Street'),
        ('Nissan of Fortworth', 'Portland', 'Oregon', '838 Coolio Drive'),
        ('Chicago CarOne', 'Chicago', 'Illinois', '83 Woopdee Doo');


INSERT INTO Cars (dealerID, reserved, make, model, body, rate)
VALUES  (1, 1, 'Honda', 'Civic', 'sedan', 43.00),
        (1, 0, 'Honda', 'Ridgeline', 'truck', 58.00),
        (2, 1, 'Jeep', 'Cherokee', 'suv', 50.00),
        (2, 0, 'Nissan', 'Camry', 'sedan', 39.00),
        (3, 0, 'Mazda', 'Miata', 'coupe', 38.00),
        (3, 1, 'Toyota', 'Prius', 'sedan', 43.00),
        (4, 1, 'Tesla', 'Model 3', 'sedan', 50.00),
        (4, 0, 'Toyota', 'Tacoma', 'truck', 52.00),
        (5, 0, 'Honda', 'Civic', 'sedan', 39.00),
        (5, 0, 'Ford', 'Expedition', 'suv', 48.00),
        (6, 1, 'Ford', 'Taurus', 'sedan', 38.00),
        (6, 1, 'Ford', 'Windstar', 'minivan', 42.00);


INSERT INTO Users (firstName, lastName, userName, passWord, cardNum, address)
VALUES	('Sammy', 'Slappy', 'samslap', 'doodaleedoo', '1234567934831234', '123 Fake Street'),
		('Buttery', 'Biscuits', 'butteryb', 'butteryPass', '7685746352419786', '89 Funkytown Drive'),
		('Bounding', 'Fishfin', 'boundFish', 'fishyPass', '9786756453647586', '76 Toasted Fudge Road');
"""