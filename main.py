"""
Main Module for EPR7 exercises.
"""

import hufftext

__author__ = "4897491: Benjamin Lucht, 2188645: Anne Schwarz"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "We would like to thank our coffee for the morning motivation."
__email__ = "9047212@stud.uni-frankfurt.de, anne@frauschwarz.org"

def main():
    t = hufftext.Huff_Text('src/John Maynard.txt')
    print(t.content)

if __name__ == '__main__':
    main()