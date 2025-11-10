from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration de la base de données (exemple avec SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ma_base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de l’ORM
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def ajouter_utilisateur():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)