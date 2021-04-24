DROP TABLE IF EXISTS Rooms;
DROP TABLE IF EXISTS Hotels;
DROP TABLE IF EXISTS Cars;
DROP TABLE IF EXISTS Dealerships;
DROP TABLE IF EXISTS Users;


CREATE TABLE Hotels (
    hotelID   INTEGER,
    name      TEXT NOT NULL,
    address   TEXT NOT NULL,
    PRIMARY KEY(hotelID)
);

CREATE TABLE Rooms (
    roomID    INTEGER,
    hotelID   INTEGER,
    num       INTEGER NOT NULL,
    reserved  INTEGER NOT NULL,
    capacity  INTEGER NOT NULL,
    PRIMARY KEY(roomID),
    FOREIGN KEY(hotelID) REFERENCES Hotels(hotelID)
);

CREATE TABLE Dealerships (
    dealerID    INTEGER,
    name        TEXT NOT NULL,
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
    PRIMARY KEY(carID),
    FOREIGN KEY(dealerID) REFERENCES Dealerships(dealerID)
);

CREATE TABLE Users (
    userID    INTEGER,
    firstName TEXT NOT NULL,
    lastName  TEXT NOT NULL,
    cardNum   TEXT,
    address   TEXT NOT NULL,
    PRIMARY KEY(userID)
);
 