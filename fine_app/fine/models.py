from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField


class Fine:
    def __init__(self, name, number_plate, violation, sum_fine, date_violation, date_payment):
        self.name = name
        self.number_plate = number_plate
        self.violation = violation
        self.sum_fine = sum_fine
        self.date_violation = date_violation
        self.date_payment = date_payment


class AddFineForm(FlaskForm):
    name = StringField('Имя')
    number_plate = StringField('Номер машины')
    violation = StringField('Причина')
    sum_fine = FloatField('Сумма штрафа')
    submit = SubmitField('Добавить штраф')


class PayFineForm(FlaskForm):
    number_plate = StringField('Номер машины')