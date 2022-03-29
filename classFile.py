
import requests

class pokemon:
    baseUrl = "https://pokeapi.co/api/v2/pokemon/"

    def __init__(self,rank):
        self.rank = rank
        
    def fetch(self):
        URL = self.baseUrl + self.rank
        data = requests.get(url = URL)
        data = data.json()
        self.name = data['name']
        self.weight = data['weight']

    def printPokemon(self):
        if(self.rank):
            print('rank = ', self.rank)

        if(hasattr(self,'name')):
            print('name = ', self.name)

        if(hasattr(self,'weight')):
            print('weight = ', self.weight)