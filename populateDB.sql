INSERT INTO Hotels (name, address)
VALUES ('Ambassador', '72 Amy Street'),
       ('Marriot', '75 West 85th Street'),
       ('Best Western', '812 Winding Brook'),
       ('Alpine Inn', '637 Real Street'),
       ('Gold Country', '718 Fake Street'),
       ('Route 78', '111 Route 78'),
       ('Claw Inn', '661 Hopping Frog'),
       ('Dockyard Place', '817 Silly Spaceman'),
       ('Kate''s Place', '85 85th Street');


INSERT INTO Rooms (hotelID, num, reserved, capacity)
VALUES  (5, 102, 1, 2),
        (4, 301, 0, 2),
        (5, 201, 0, 3),
        (6, 104, 0, 2),
        (6, 202, 0, 4),
        (7, 103, 1, 2),
        (7, 202, 1, 4),
        (8, 301, 0, 3),
        (8, 204, 0, 2),
        (9, 101, 0, 3),
        (9, 204, 1, 2),
        (1, 103, 1, 2),
        (2, 201, 0, 2),
        (2, 101, 0, 4),
        (1, 250, 1, 2),
        (3, 300, 0, 4),
        (4, 500, 0, 2);


INSERT INTO Dealerships (name, address)
VALUES  ('First Texas Honda', '728 George Street'),
        ('Toyota of Austin', '23 Salmon Lane'),
        ('Tesla', '838 Led Zeppelin Drive'),
        ('Classic Chevrolet', '910 Big Street'),
        ('Nissan of Fortworth', '838 Coolio Drive'),
        ('Texas CarOne', '83 Woopdee Doo');


INSERT INTO Cars (dealerID, reserved, make, model, body)
VALUES  (1, 1, 'Honda', 'Civic', 'sedan'),
        (1, 0, 'Honda', 'Ridgeline', 'truck'),
        (2, 1, 'Jeep', 'Cherokee', 'suv'),
        (2, 0, 'Nissan', 'Camry', 'sedan'),
        (3, 0, 'Mazda', 'Miata', 'coupe'),
        (3, 1, 'Toyota', 'Prius', 'sedan'),
        (4, 1, 'Tesla', 'Model 3', 'sedan'),
        (4, 0, 'Toyota', 'Tacoma', 'truck'),
        (5, 0, 'Honda', 'Civic', 'sedan'),
        (5, 0, 'Ford', 'Expedition', 'suv'),
        (6, 1, 'Ford', 'Taurus', 'sedan'),
        (6, 1, 'Ford', 'Windstar', 'minivan');


INSERT INTO Users (firstName, lastName, cardNum, address)
VALUES	('Sammy', 'Slappy', '1234567934831234', '123 Fake Street'),
		('Buttery', 'Biscuits', '7685746352419786', '89 Funkytown Drive'),
		('Bounding', 'Fishfin', '9786756453647586', '76 Toasted Fudge Road');
