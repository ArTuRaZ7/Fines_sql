from flask import render_template, request
from fine_app import app, DB_PATH
from fine_app.fine.models import Fine, AddFineForm, PayFineForm
import datetime
import sqlite3


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddFineForm()

    #Получаем данные и пихаем в базу
    if request.method == 'POST':
        name = form.name.data
        number_plate = form.number_plate.data
        violation = form.violation.data
        sum_fine = form.sum_fine.data
        date_violation = str(datetime.date.today())


        try:
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()
            cursor.execute(f'''
            INSERT INTO fine(name, number_plate, violation, sum_fine, date_violation) 
            VALUES('{name}', '{number_plate}', '{violation}', {sum_fine}, '{date_violation}')
            ''')
            connection.commit()
            cursor.close()

        except sqlite3.Error as error:
            print('Не удалось подключиться к бд', error)

        finally:
            if connection:
                connection.close()


    return render_template('add_fine.html', form=form)


@app.route('/fines')
def fines():
    all_fines = []
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute(
            '''
            SELECT name, number_plate, violation, sum_fine, date_violation, date_payment FROM fine
            ''')

        for fine in cursor.fetchall():
            current_fine = Fine(*fine)
            all_fines.append(current_fine)

    except sqlite3.Error as error:
        print('Неудалось подключиться к дб', error)
    finally:
        if connection:
            connection.close()

    return render_template('fines.html', fines=all_fines)

@app.route('/pay', methods=['GET', 'POST'])
def pay():
    if 'Артуру было лень':
        return render_template('pay.html')