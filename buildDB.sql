DROP TABLE IF EXISTS Hotels;
DROP TABLE IF EXISTS Rooms;
DROP TABLE IF EXISTS Dealerships;
DROP TABLE IF EXISTS Cars;
DROP TABLE IF EXISTS Users;


CREATE TABLE Hotels (
    hotelID   INTEGER,
    name      TEXT NOT NULL,
    PRIMARY KEY(hotelID)
);

INSERT INTO Hotels VALUES (1, 'Ambassador');
INSERT INTO Hotels VALUES (2, 'Marriot');
INSERT INTO Hotels VALUES (3, 'Best Western');
INSERT INTO Hotels VALUES (4, 'Alpine Inn');
INSERT INTO Hotels VALUES (5, 'Gold Country');
INSERT INTO Hotels VALUES (6, 'Route 78');
INSERT INTO Hotels VALUES (7, 'Claw Inn');
INSERT INTO Hotels VALUES (8, 'Dockyard Place');


CREATE TABLE Rooms (
    roomID    INTEGER,
    hotelID   INTEGER,
    num       INTEGER NOT NULL,
    reserved  INTEGER NOT NULL,
    capacity  INTEGER NOT NULL,
    PRIMARY KEY(roomID),
    FOREIGN KEY(hotelID) REFERENCES Hotels(hotelID)
);

INSERT INTO Rooms VALUES (1, 1, 101, 0, 4);
INSERT INTO Rooms VALUES (2, 2, 250, 1, 2);
INSERT INTO Rooms VALUES (3, 3, 300, 0, 4);
INSERT INTO Rooms VALUES (4, 1, 500, 0, 2);

CREATE TABLE Dealerships (
    dealerID   INTEGER,
    name       TEXT NOT NULL,
    PRIMARY KEY(dealerID)
);

INSERT INTO Dealerships VALUES (1, 'First Texas Honda');
INSERT INTO Dealerships VALUES (2, 'Toyota of Austin');
INSERT INTO Dealerships VALUES (3, 'Tesla');

CREATE TABLE Cars (
    carID     INTEGER,
    dealerID  INTEGER,
    reserved  INTEGER NOT NULL,
    body      TEXT NOT NULL,
    PRIMARY KEY(carID),
    FOREIGN KEY(dealerID) REFERENCES Dealerships(dealerID)
);

CREATE TABLE Users (
    userID    INTEGER,
    firstName TEXT NOT NULL,
    lastName  TEXT NOT NULL,
    cardNum   INTEGER,
    address   TEXT NOT NULL,
    PRIMARY KEY(userID)
);

INSERT INTO Users VALUES (1, 'Sammy', 'Slappy', 1234567934831234, '123 Fake Street');
INSERT INTO Users VALUES (1, 'Buttery', 'Biscuits', 7685746352419786, '89 Funkytown Drive');
INSERT INTO Users VALUES (1, 'Bounding', 'Fishfin', 9786756453647586, '76 Toasted Fudge Road');

