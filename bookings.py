# import modules
import argparse
import sqlite3
from sqlite3 import Error
from tkinter import *
import os
import queries  # holds the SQL queries for out database

DB = 'data.db'  # database name


# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    rdb = r"{0}".format(os.path.expanduser(db_file))
    try:
        conn = sqlite3.connect(rdb)
        conn.row_factory = sqlite3.Row
    except Error as e:
        raise e

    return conn


def run_query(sql):
    """execute query and return results

    good for performing searches on the database

    :param sql:
    :return:
    """
    print('SQL: ' + sql)
    conn = create_connection(DB)
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Found {0} results".format(len(results)))
    cursor.close()
    return results


def run_commit_query(sql):
    """execute query then commit to database

    good for updating, inserting or deleting

    :param sql:
    :return:
    """
    print('SQL: ' + sql)
    conn = create_connection(DB)
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Found {0} results".format(len(results)))
    cursor.close()
    conn.commit()
    return results


def getUserID(att, val):
    query = queries.getUserID(att, val)
    results = run_query(query)
    for row in results:
        return row[str('userID')]


def createAccount(firstName, lastName, userName, passWord, cardNum, address):
    query = queries.insertAccount(firstName, lastName, userName, passWord, cardNum, address)
    run_commit_query(query)


def updateAccount(id, att, newVal):
    query = queries.updateAccount(id, att, newVal)
    run_commit_query(query)


def createHotelListing(name, city, state, address):
    query = queries.insertHotel(name, city, state, address)
    run_commit_query(query)


def resetDB():
    query = queries.resetDB()
    run_commit_query(query)


def test_createAccount():
    print("Testing insertion of 3 new accounts")
    createAccount('Timmy', 'Tuna', 'ttuna', 'tunasPass', '1726869584736152', '88 Backgammon Blvd')
    createAccount('Michelle', 'Sleepy', 'sleepym', 'michelleiscool', '8675647362514253', '548 Next Door Street')
    createAccount('Dingus', 'Tractor', 'dingust', 'dingusHasApass', '8675647361524352', '789 Cant Remember Drive')
    print("3 accounts successfully added")


def test_createHotelListing():
    print("Testing insertion of 3 hotel listings")
    createHotelListing('Creepy Hotel', 'Area 51', 'New Mexico', '123 Alien Drive')
    createHotelListing('Ritz Carlton', 'New York', 'New York', '85 Fancypants Lane')
    createHotelListing('Four Seasons', 'Miami', 'Florida', '987 Coolio Drive')
    print("3 hotel listings created successfully")


def test_updateAccount():
    userID = getUserID('userName', 'butteryb')
    updateAccount(userID, 'address', '110 Funkytown Drive')


def parse_args():
    parser = argparse.ArgumentParser(description="Bookings Website")
    parser.add_argument('-ca', '--createaccount', dest='createAccount', action='store_true',
                        help='create a dummy account')
    parser.add_argument('-rdb', '--resetdb', dest='resetdb', action='store_true',
                        help='reset the database')
    parser.add_argument('-thl', '--testCreateHotelListing', dest='test_createHotelListing', action='store_true',
                        help='test inserting hotel listings')
    parser.add_argument('-ua', '--updateaccount', dest='updateAccount', action='store_true',
                        help='create a dummy account')
    parser.add_argument('-su', '--searchusers', dest='searchUsers', nargs='?', default=None,
                        help='search database for username')
    parser.add_argument('-hs', '--hotelsbystate', dest='hotelsByState', nargs='?', default=None,
                        help='search database for hotels in a state')
    parser.add_argument('-hc', '--hotelsbycity', dest='hotelsByCity', nargs='?', default=None,
                        help='search database for hotels in a city')
    return parser.parse_args()


def main():
    print('...starting main...')

    args = parse_args()

    if args.searchUsers:
        username = args.searchUsers
        query = queries.searchUserName(username)
        results = run_query(query)

        print('NAME\t\t\t\tCARD NUMBER\t\t\tADDRESS')
        for row in results:
            print(row[str('firstName')] + ' ' +
                  row[str('lastName')] + '\t' +
                  row[str('cardNum')] + '\t' +
                  row[str('address')])
        return 0

    if args.hotelsByState or args.hotelsByCity:

        if args.hotelsByState:
            query = queries.getHotelsByState(args.hotelsByState)
        else:
            query = queries.getHotelsByCity(args.hotelsByCity)

        results = run_query(query)

        print('NAME\t\t\tCITY\t\tSTATE\t\tADDRESS')
        for row in results:
            print(row[str('name')] + '\t\t' +
                  row[str('city')] + '\t\t' +
                  row[str('state')] + '\t\t' +
                  row[str('address')])
        return 0

    if args.createAccount:
        test_createAccount()
        return 0

    if args.updateAccount:
        test_updateAccount()
        return 0

    if args.test_createHotelListing:
        test_createHotelListing()
        return 0

    main_account_screen()


if __name__ == "__main__":
    main()
