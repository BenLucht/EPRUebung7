"""
Text module, implements a text class for storing text and statistics on the text.
"""

__author__ = "4897491: Benjamin Lucht, 2188645: Anne Schwarz"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "We would like to thank our coffee for the morning motivation."
__email__ = "9047212@stud.uni-frankfurt.de, anne@frauschwarz.org"

import itertools

class Text():
    def __init__(self, path):
        """
        Reads text from a file, stores it.
        """

        #list of common encodings to try (taken from EPR6, moved ascii to #1)
        codec_list = itertools.chain(['ascii', 'utf-32', 'utf-16', 'utf-8','latin-1'])

        #tries reading file with different encodings, saving first match
        while True:
            try:
                self.decoded_as = next(codec_list)
                with open(path, 'r', encoding=self.decoded_as, errors='strict') as text:
                    self.content = text.read()
                    break
            except:
                pass

    def distribution_characters(self):
        """Calculates the frequency distribution of characters."""
        total = len(self.content)
        #list of tuples (char, freq)
        temp = [(item, self.content.count(item), self.content.count(item)*1.0/total, 0) \
                for item in set(self.content)]

        #sorts the list of tuples by frequency
        return sorted(temp, key=lambda t: t[1])[::-1]

if __name__ == '__main__':
    pass