# Installer cette application

> pip install -r requirements.txt

# Executer cette application

> export FLASK_APP=hello.py
> flask run

# Objectifs de la journée
Ensemble, nous allons développer une petite application en Python. 
L'objectif est d'utiliser Flask et de réaliser un petit serveur web. 

Pour ce faire, nous sommes partis sur une base de données existante, les
 personnes présentes au sein du Titanic le jour du tragique incident.
 
Ensemble, nous allons : 
 - Créer un formulaire permettant de saisir une de ces personnes
 - Lister les personnes existantes
 - Visualiser un enregistrement issu de la base de données. 
 
Si vous souhaitez avoir un aperçu des données manipulées, vous avez au sein
 de ce dépôt le fichier `titanic.csv` le fichier qui est initialement import
 é au sein de la base de données.


## Exercice 1 : Faire fonctionner flask
Cet exercice porte sur l'execution du  python et faire fonctionner une
 petite application web. 
 
Au sein de votre IDE préféré, créez un fichier `hello.py`.
Ce fichier devra contenir le code suivant : 

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
```

Votre IDE devrait vous permettre de lancer ce script directement. 
Si ce n'est pas le cas, vous pouvez aussi lancer ce script depuis un console
 en éxecutant la commande `python hello.py`.

## Exercice2 : Utiliser des templates.
Pour le moment, notre interface graphique est assez limitée. En effet, nous
 avons la tendance en informatique de décoreller la logique de l'interface. 
 
Ajoutons donc maintenant des templates pour générer nos pages html. 

A la racine de ce projet, créer deux dossiers `templates` et `static`
Créer la page `templates/index.html` contenant :
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello HTML Templates</title>
    <link rel="stylesheet"
          href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

<div>

    <h1>Hello, {{ name }}!</h1>

    <p>Change the name in the <em>browser address bar</em>
        and reload the page.</p>

</div>

</body>
</html>
```
Ainsi qu'un fichier vide `static/style.css`.
Nous pouvons maintenant utiliser ce template au sein de notre fichier
 principal : 
 
```python
from flask import Flask, render_template
# [...]
@app.route('/template/<name>')
def template(name):
    return render_template('index.html', name=name)
```

Plusieurs choses sont à voir ici, les paramètres d'url ainsi que la
 passation d'un paramètre au template.
 
## Exercice 3 : Intégrer un formulaire de saisie
Nous allons ajouter la route `/addTitanicRecord`, permettant de rajouter un
 personne ayant subit le naufrage. 
 

Il est tout à fait possible de gérer le formulaire au sein de notre HTML n
éanmoins, afin de pouvoir le manipuler plus facilement depuis notre python
, et continuer à dissocier la forme du fond, nous allons gérer la structure
 de l'objet depuis python.
 
 Créer une classe TitanicUserForm, ainsi que la route associée. 
 Pour que le formulaire soit correctement interprêté par le template, nous
  allons utiliser deuxnouvelles bibliothèques flask_wtf et flask_bootstrap.
 
```python 
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, BooleanField, IntegerField, \
    SelectField, DecimalField
from wtforms.validators import DataRequired, NumberRange
# [....] 
app.config['SECRET_KEY'] = 'this is a secret'
Bootstrap(app)

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

@app.route('/titanic/add')
def addTitanicRecord():
    form = TitanicUserForm()
    return render_template('titanic.html', form=form)
```

Agrémenté par le template `templates/titanic.html`

```html
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block styles %}
{{ super() }}
	<style>
		body { background: #e8f1f9; }
	</style>
{% endblock %}


{% block title %}
Add a titanic member
{% endblock %}


{% block content %}
    {{ wtf.quick_form(form) }}
{% endblock %}
```
## Exercice 4 : Créer la base de données
Une fois que nous avons un formulaire, il est souvent d'usage de sauvegarder
 ce qui a été saisi au sein d'une base de données.
Il est possible de considérer un fichier Excel ou CSV comme une base de donn
ées. 
Néanmoins, les bases de données en tant que telles nous permettent de mieux
 manipuler les données. 
L'objectif de cette étape est donc de créer une base de données avec une
 table ayant la  structure suivante : 
 
 ```
import sqlite3
# [...]
database_conn = None # DB Connector
database_filename = 'database.sqlite'

# [...]
if __name__ == '__main__':
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
``` 

N'oubliez pas de vérifier l'état de votre base de données. Le fichier est-il
 créé. Contient-il une table ayant la structure attendue etc... 
 
## Exercice 5: Importer la données
Nous avons déjà de la donnée disponible au sein du fichier CSV. Faites en
 sorte pour que lors de la création de la base de données. Si la table n
 'existe pas, alors elle est automatiquement générée et alimentée.

```python
import csv
csv_file = 'titanic.csv'
data_from_csv = csv.DictReader(open(csv_file, "r", encoding="utf-8"), delimiter
=';', quotechar='"')
query = "INSERT INTO TITANIC (Survived, Pclass, Name, Sex, Age,SibSp, " \
            "Parch,  Ticket,Fare, Cabin, Embarked) VALUES " \
            "({Survived}, {Pclass},'{Name}', '{Sex}', {Age}, {SibSp}, " \
            "{Parch}, '{Ticket}',{Fare}, '{Cabin}', '{Embarked}')"


for record in data_from_csv:
     cur = database_conn.cursor()
     cur.execute(query.format(**record))
     database_conn.commit()
```

## Exercice 6: Associez votre formulaire à la base de données. 
Il ne reste plus qu'à stocker au sein de la base de données ce qui a ét
é saisi au sein de votre formulaire. 

Pour celà vous devrez écouter la méthodes associée à la route 
```python
@app.route('/titanic/add', methods=['GET', 'POST'])
def addTitanicRecord():
    form = TitanicUserForm()
    if form.validate_on_submit():
        # TODO
        # Gérer votre insertion, en réalisant la requête au sein de la BDD
        # Puis effacez le formulaire en cours en faisant la redirection suivante:
        redirect(url_for('addTitanicUser'))
    return render_template('titanic.html', form=form)
```
## Exercice 7: Ajoutez un page qui liste l'ensemble des personnes présentes dans la base de données.
C'est à vous de jouer maintenant. Appropriez vous l'outil et la technologie
 afin de lister l'ensemble des enregistrements issus de la base de données. 
 
 ```python
@app.route('/titanic/add', methods=['GET'])
def listTitanicRecord:
    pass
```

## Exercice 8: Ajouter une page qui affiche un enregistrement issu de la base de données.
 ```python
@app.route('/titanic/<id>')
def getTitanicRecord(id):
    # TODO
    pass
``` 