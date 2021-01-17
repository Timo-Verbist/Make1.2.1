#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "finished"

from datetime import datetime


def main():
    leeftijd = int(input("geef je leeftijd aub.\n"))
    maand = int(input("geef ook de maand waarin je verjaart (getal).\n"))
    if maand > 12:
        print("er zijn maar 12 maanden.")
    if maand < 13 & maand > int(datetime.now().strftime('%m')):
        geboortejaar = int(datetime.now().strftime('%Y')) - leeftijd - 1
        print("u bent geboren in " + str(geboortejaar))
    elif maand < int(datetime.now().strftime('%m')):
        geboortejaar = int(datetime.now().strftime('%Y')) - leeftijd
        print("u bent geboren in " + str(geboortejaar))
    elif maand == int(datetime.now().strftime('%m')):
        dag = int(input("geef ook de dag waarop je verjaart (getal).\n"))
        if dag < 31 & dag > int(datetime.now().strftime('%d')):
            geboortejaar = int(datetime.now().strftime('%Y')) - leeftijd - 1
            print("u bent geboren in " + str(geboortejaar))
        elif dag <= int(datetime.now().strftime('%d')):
            geboortejaar = int(datetime.now().strftime('%Y')) - leeftijd
            print("u bent geboren in " + str(geboortejaar))
        elif dag > 31:
            print("er zijn maximum 31 dagen in een maand.")

    if leeftijd < 50:
        print("U wordt 50 jaar in " + str(geboortejaar + 50) + ".")
    elif leeftijd > 50:
        print("U bent 50 jaar geworden in " + str(geboortejaar + 50) + ".")
    elif leeftijd == 50:
        print("U bent dit jaar 50 geworden of u wordt dit jaar 50.")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
