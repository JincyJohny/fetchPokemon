from classFile import *

def main():
    n = input("Enter the count of pokemons: ")
    N = int(n)
    for i in range(0,N):
        rank = input("Enter the rank: ")   
        newObj = pokemon(rank)
        newObj.fetch()
        newObj.printPokemon()

if (__name__ == "__main__"):
    main()