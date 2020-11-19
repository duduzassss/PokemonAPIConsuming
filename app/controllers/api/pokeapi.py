import db 

from url_api import url
import requests, json

def acess_api(url):
    requisicao = requests.get(url)
    resposta = json.loads(requisicao.text)
    result = resposta["results"]
    # print(result)
    return result


def record_name_pokemon():
    lista_pokemons = acess_api(url)
    
    for n in lista_pokemons:
        dicio = {"name": n["name"]}
        print(n)
        for value in dicio.values():
            ...
            # print(value)
            # name_pokemon = ImagePokemon(
            #                 name = value,
            #                 link_img = 
            # )
            



record_name_pokemon()