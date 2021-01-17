#!/usr/bin/env python
"""
Een python script dat eerst een voorgeprogrammeerde lijst weergeeft, daarna om een willekeurig aantal woorden vraagt en deze ook in een lijst steekt en weergeeft.
Dit ZONDER een loop en beroep te doen op de 'seperator'.
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "finished"

# import


def main():
    random_list = ["apple", "ps5", "samsung", "bicicle", "Big Ben"]
    print(random_list)
    aantal = int(input("Hoeveel woorden wilt u geven?\n"))
    for i in range(aantal):
        woord = str(input("Geef een woord aub.\n"))
        random_list.append(woord)
    print(random_list)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
