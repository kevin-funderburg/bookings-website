import unittest
import bookings
import sqlite3


class MyTestCase(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(1+1, 2, "it's working")

    def CheckSqliteRowIndex(self):
        con = sqlite3.connect(bookings.DB)
        con.row_factory = sqlite3.Row
        row = con.execute("select 1 as a, 2 as b").fetchone()
        self.assertTrue(isinstance(row,
                                   sqlite3.Row),
                        "row is not instance of sqlite.Row")

        col1, col2 = row["a"], row["b"]
        self.assertTrue(col1 == 1, "by name: wrong result for column 'a'")
        self.assertTrue(col2 == 2, "by name: wrong result for column 'a'")

        col1, col2 = row["A"], row["B"]
        self.assertTrue(col1 == 1, "by name: wrong result for column 'A'")
        self.assertTrue(col2 == 2, "by name: wrong result for column 'B'")

        col1, col2 = row[0], row[1]
        self.assertTrue(col1 == 1, "by index: wrong result for column 0")
        self.assertTrue(col2 == 2, "by index: wrong result for column 1")

    def test_search_hotels_by_city(self):
        bookings.getHotelsByCity('Austin')

    def test_createAccount(self):
        bookings.createAccount('Timmy', 'Tuna', 'ttuna', 'tunasPass', '1726869584736152', '88 Backgammon Blvd')
        bookings.createAccount('Michelle', 'Sleepy', 'sleepym', 'michelleiscool', '8675647362514253', '548 Next Door Street')
        bookings.createAccount('Dingus', 'Tractor', 'dingust', 'dingusHasApass', '8675647361524352', '789 Cant Remember Drive')

    def test_updateAccount():
        userID = bookings.getUserID('userName', 'butteryb')
        bookings.updateAccount(userID, 'address', '110 Funkytown Drive')

    def test_createHotelListing():
        print("Testing insertion of 3 hotel listings")
        createHotelListing('Creepy Hotel', 'Area 51', 'New Mexico', '123 Alien Drive')
        createHotelListing('Ritz Carlton', 'New York', 'New York', '85 Fancypants Lane')
        createHotelListing('Four Seasons', 'Miami', 'Florida', '987 Coolio Drive')
        print("3 hotel listings created successfully")


if __name__ == '__main__':
    unittest.main()
