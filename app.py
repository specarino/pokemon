import requests
import random


def pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/"

    total = requests.get(url).json()["count"]
    pokemon = random.randint(1, total)
    response = requests.get(f"{url}{pokemon}").json()["name"]

    return response


if __name__ == "__main__":
    print(pokemon())
