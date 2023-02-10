"""
SQLLite dabatabase management.
"""
import sqlite3
import csv
from os.path import exists

database_conn = None # DB Connector

def generate_data():
    """
    Generate data fro the titanic.csv file and filling in the records in the sqlite file.
    This should only occur on first launch if the db file was missing.
    :return:
    """
    csv_file = 'titanic.csv'
    data_from_csv = csv.DictReader(open(csv_file, "r", encoding="utf-8"),
                                   delimiter
                                   =';', quotechar='"')
    query = "INSERT INTO TITANIC (Survived, Pclass, Name, Sex, Age,SibSp, " \
            "Parch,  Ticket,Fare, Cabin, Embarked) VALUES " \
            "({Survived}, {Pclass},'{Name}', '{Sex}', {Age}, {SibSp}, " \
            "{Parch}, '{Ticket}',{Fare}, '{Cabin}', '{Embarked}')"

    for record in data_from_csv:
        cur = database_conn.cursor()
        # print(record)
        cur.execute(query.format(**record))
        database_conn.commit()



def create_db_if_not_exists(database_filename):
    """
        Check if the given sqlite database exists.
        If not, it generates it and fills it with data.
    """
    new_database = not exists(database_filename)
    database_conn = sqlite3.connect(database_filename)
    database_conn.execute('''CREATE TABLE IF NOT EXISTS TITANIC
                     (PassengerId INTEGER PRIMARY KEY  AUTOINCREMENT    NOT NULL,
                     Survived TINYINT    NOT NULL,
                     Pclass TINYINT NOT NULL,
                     Name VARCHAR(50) NOT NULL,
                     Sex VARCHAR(6),
                     Age REAL DEFAULT 0.00,
                     SibSp INT,
                     Parch INT,
                     Ticket VARCHAR(50),
                     Fare REAL,
                     Cabin VARCHAR(50),
                     Embarked REAL);''')
    if new_database:
        generate_data()