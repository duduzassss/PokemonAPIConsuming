from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config') # Passando as configs do arquivo config.py

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Importando no flask os controllers depois da instancia
# de app, pq precisamos que ela já esteja declarada, 
# pois usamos a variável app nos nossos módulos
from app.controllers import default