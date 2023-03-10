from flask import Flask, render_template, request
import MySQLdb
from flaskext.mysql import MySQL
import datetime

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'jolieboite'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def formulaire():
    return render_template('form.html')

@app.route('/register', methods=['POST'])
def register():
    nomUtilisateur = request.form['nomUtilisateur']
    mdp = request.form['mdp']
    
    # Save the data to the MySQL database
    conn = mysql.connect()
    cursor = conn.cursor()

    # Sélectionnez la valeur maximale de idUtilisateur dans la table Utilisateur
    cursor.execute('SELECT MAX(idUtilisateur) FROM Utilisateur')
    result = cursor.fetchone()

    # Si la table est vide, commencez à 1, sinon incrémentez la valeur maximale de idUtilisateur
    if result[0] is None:
        idUtilisateur = 1
    else:
        idUtilisateur = result[0] + 1

    # Insérez une nouvelle ligne dans la table Utilisateur avec l'idUtilisateur auto-incrémenté
    cursor.execute('INSERT INTO Utilisateur (idUtilisateur, nomUtilisateur, mdp) VALUES (%s, %s, %s)', (idUtilisateur, nomUtilisateur, mdp))
    conn.commit()
    conn.close()

    return render_template('success.html', nomUtilisateur=nomUtilisateur, mdp=mdp)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/inscriptioncontacts')
def inscriptioncontacts():
    return render_template('inscriptioncontacts.html')

@app.route('/inscriptionboites')
def inscriptionboites():
    return render_template('inscriptionboites.html')

if __name__ == '__main__':
    app.run(debug=True)