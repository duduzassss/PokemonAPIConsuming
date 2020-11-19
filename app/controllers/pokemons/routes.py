from flask import Flask, render_template

import requests, json
from random import randint

from app import app



@app.route('/pokemons')
def pokemons():
    try:
        lista_nome = []
        lista_url = []
        for j in range(0,6):
            requisicao = requests.get("https://pokeapi.co/api/v2/pokemon?limit=7") #1050
            resposta = json.loads(requisicao.text) # Transform in dict iterable
            pokemon  = resposta["results"]
            
        dados = []
        for p in pokemon:
            req = requests.get(p["url"])
            res = json.loads(req.text)
            poke = res["sprites"]["other"]["official-artwork"]["front_default"]
            dicio = {"name": p["name"], "img": poke}
            dados.append(dicio)
             
        return render_template('pokemons/pokemons.html', dados = dados) #lista_image = lista_image, lista_nome = lista_nome
    except:
        return 'Error'