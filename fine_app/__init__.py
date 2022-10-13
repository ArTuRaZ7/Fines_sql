from flask import Flask
import os
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ewhretyk43y5eh'
DB_PATH = os.path.abspath('database.db')

if not os.path.isfile(DB_PATH):
    try:
        sqlite_connection = sqlite3.connect(DB_PATH)
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к SQLite")
        cursor.execute('''
            CREATE TABLE fine(
                fine_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50),
                number_plate VARCHAR(6),
                violation VARCHAR(50),
                sum_fine DECIMAL(8,2),
                date_violation DATE,
                date_payment DATE
            );
        ''')

    except sqlite3.Error as error:
        print('Ошибка при подключении к sqlite', error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()

import fine_app.fine.views