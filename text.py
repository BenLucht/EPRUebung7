"""
Text module, implements a text class for storing text and statistics on the text.
"""

__author__ = "xxxxxxx: Ben, xxxxxxx: Anne"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "We would like to thank our coffee for the morning motivation."
__email__ = "xxxxxxxx@stud.uni-frankfurt.de, xxxxxxxx@stud.uni-frankfurt.de"

import string
import itertools
import re
import json
import os
import time

class text():
    def __init__(self, path):
        """
        Reads text from a file, stores it and text statistics such as:
        word_count : amount of full words in the text (excl. apostrophed additions)
        keystroke_count : total amount of keystrokes needed to produce the text
        character_count : amount of characters in the text (excl. spaces)
        character_distribution : frequency distribution of characters in the text
        word_distribution : frequency distribution of words in the text
        average_word_length : average length of the words in the text
        """

        #list of common encodings to try
        codec_list = itertools.chain(['utf-32', 'utf-16', 'utf-8', 'ascii', 'latin-1'])

        #tries reading file with different encodings, saving first match
        while True:
            try:
                self.decoded_as = next(codec_list)
                with open(path, 'r', encoding=self.decoded_as, errors='strict') as text:
                    self.content = text.read()
                    break
            except:
                pass

    def count_characters(self, content):
        """Counts all characters excl. spaces."""

        #everything but whitespace of any kind
        chars = re.compile(r'\S')

        return len(chars.findall(content))


if __name__ == '__main__':
    pass