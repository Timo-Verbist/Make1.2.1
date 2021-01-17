#!/usr/bin/env python
"""
Een python script dat als output het aantal tekens geeft van de ingegeven string.
Het script vraagt om een willekeurig woord in te geven en geeft als output het aantal tekens terug.
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "finished"

# import


def main():
    while True:
        number = 0
        word = str(input("Geef iets in aub.\n"))
        for i in word:
            number += 1
        print("De lengte van uw string is: " + str(number) + "\n")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
