# https://pokeapi.co/

import requests


def get_pokemon(url="https://pokeapi.co/api/v2/pokemon-form/", offset=0):
    args = {"offset": offset} if offset else {}
    response = requests.get(url, params=args)

    if response.status_code == 200:
        payload = response.json()
        results = payload.get("results", [])

        if results:
            for pokemon in results:
                name = pokemon["name"]
                print(name)

        next = input("¿Continuar Listado? [y/n] \n").lower()
        if next == "y":
            get_pokemon(offset=offset + 20)


get_pokemon()
