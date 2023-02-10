from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, \
    SelectField, DecimalField
from wtforms.validators import DataRequired, NumberRange

class TitanicUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    survived = BooleanField('Has Survived ?')
    pclass = IntegerField('Class rate', validators=[NumberRange(1, 3)])
    sex = SelectField('Sex', choices=['male', 'female'])
    age = DecimalField('Age')
    sibsp = IntegerField('SibSp')
    parch = IntegerField('Parch')
    ticket = StringField('Ticket')
    fare = DecimalField('Fare')
    cabin = StringField('Cabin')
    embarked = StringField('Embarked')
    submit = SubmitField('Submit')