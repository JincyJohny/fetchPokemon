from classFile import *


def main():
    rank = input("Enter the rank: ")
    newObj = pokemon(rank)
    newObj.fetch()
    newObj.printPokemon()


if (__name__ == "__main__"):
    main()
