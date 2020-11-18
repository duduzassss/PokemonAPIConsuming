from flask import Flask, render_template

import requests, json

from app import app



@app.route('/pokemons')
def pokemons():
    try:
        requisicao = requests.get("https://pokeapi.co/api/v2/pokemon?limit=6")
        resposta = json.loads(requisicao.text)
        pokemons  = resposta["results"]
        
        lista = []
        for pokemon in pokemons:
            for i in pokemon:
                ...
                # print(type(pokemon[i]))
            # print(pokemon[i])
            
            url_pokemon = requests.get(pokemon[i])
            resp = json.loads(url_pokemon.text)
            resp2 = resp["sprites"]["other"]["official-artwork"]["front_default"]
            # print(resp2)
            lista.append(resp2)
            print(lista)
            
        # return '200'
        return render_template('pokemons/pokemons.html', lista = lista)
    except:
        return 'Error'