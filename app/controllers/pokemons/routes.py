from flask import Flask, render_template

import requests, json
from random import randint

from app import app, db
from app.models.models import ImagePokemon

from string import Template # importação do join
from sqlalchemy import text


@app.route('/pokemons')
def pokemons():
    lista_nome = []
    lista_url = []
    # for j in range(0,6):
    requisicao = requests.get("https://pokeapi.co/api/v2/pokemon?limit=50") #1050
    resposta = json.loads(requisicao.text) # Transform in dict iterable
    pokemon  = resposta["results"]
        
    dados = []
    for p in pokemon:
        req = requests.get(p["url"])
        res = json.loads(req.text)
        poke = res["sprites"]["other"]["official-artwork"]["front_default"]
        dicio = {"name": p["name"], "img": poke}
        dados.append(dicio)
        # print(dados[0]["name"])
        
        
    for i in range(0,len(dados)):
        # print(dados[i])
        p = ImagePokemon.query.filter_by(name=dados[i]["name"]).first()
        if p is None:
            save_pokemon = ImagePokemon(
                            name = dados[i]["name"],
                            link_img = dados[i]["img"]
            )
            db.session.add(save_pokemon)
            db.session.commit()
            
    send_pokemons = ImagePokemon.query.all()
    # print(send_pokemons[0])
    
    
        
            
    return render_template('pokemons/pokemons.html', send_pokemons = send_pokemons) #lista_image = lista_image, lista_nome = lista_nome
