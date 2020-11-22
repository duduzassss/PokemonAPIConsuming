from flask import Flask, render_template

import requests, json
from random import randint

from app import app, db
from app.models.models import ImagePokemon

from string import Template # importação do join
from sqlalchemy import text
import time


def conectAPI():
    requisicao = requests.get("https://www.canalti.com.br/api/pokemons.json")
    resposta = json.loads(requisicao.text) # Transform in dict iterable
    
    return resposta

@app.route('/pokemons')
def pokemons():
    resposta = conectAPI()
    pokemons  = resposta["pokemon"]
    
   
    lista_pokemons = []
    for pokemon in pokemons:
        dicio = {"num": pokemon["num"],"name": pokemon["name"],"img": pokemon["img"], "type": pokemon["type"]}
        lista_pokemons.append(dicio)
            
    return render_template('pokemons/pokemons.html', lista_pokemons = lista_pokemons) #send_pokemons = send_pokemons

@app.route('/pokemon/<name>')
def pokemon(name):
    resposta = conectAPI()
    pokemons = resposta["pokemon"]
    
    pokemon = str(name).capitalize()
    #print(pokemon) #bulbasaur
    
    try:
        for poke in pokemons: # return multiples dict
            if pokemon in poke["name"]:
                lista = []
                lista.append(poke)
                print(lista)

               

                return render_template('pokemons/single_pokemon.html', lista = lista)
                
    except:
        print("Error: Pokémon name is not in API.")

    
    