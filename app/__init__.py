from flask import Flask

app = Flask(__name__)

# Importando no flask os controllers depois da instancia
# de app, pq precisamos que ela já esteja declarada, 
# pois usamos a variável app nos nossos módulos
from app.controllers import default