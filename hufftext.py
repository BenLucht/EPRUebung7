"""
Huff_Text module, implements a text class for implementing Huffman coding.
"""

__author__ = "4897491: Benjamin Lucht, 2188645: Anne Schwarz"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "We would like to thank our coffee for the morning motivation."
__email__ = "9047212@stud.uni-frankfurt.de, anne@frauschwarz.org"

import csv
import text
import tree

class Huff_Text(text.Text):
    """Huff_Text class extends capabilities of Text to accomodate Huffman coding."""

    def __init__(self, plain_text=None, bin_text=None, csv_file=None):
        """Makes Huff_Text object from either plain text or or coded text + statistics."""
        if plain_text is not None:
            super().__init__(plain_text)
            self.stats = self.distribution_characters()
            self.huff_code = self.make_huff_code()
        elif plain_text is None and bin_text is not None and csv_file is not None:
            #not implemented
            pass
        else:
            print('Please either enter a plain text file name or'
                  'a binary encoded text file + corresponding csv file.')

    def make_huff_code(self):
        """Function returns dictionary {huff_code:character}."""
        nodes = []
        #makes a tree node for each character in text statistics
        for char, _, wgt, _ in self.stats:
            nodes.append(tree.Node(character=char, weight=wgt))

        maker = tree.Tree_Maker(nodes) #calls TreeMaker to make tree from nodes

        return maker.make_dict()

    def save_files(self, coded_file_name):
        """Saves a coded_file_name.csv and coded_file_name.bin file."""

        with open(coded_file_name+'.csv', 'w') as csvfile:
            print('writing csv')
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Zeichen', 'Absolute Häufigkeit', 'Relative Häufigkeit',\
                                 'Informationsgehalt dieses Zeichens'])
            for char_stats in self.stats:
                spamwriter.writerow(char_stats)

        with open(coded_file_name+'.bin', 'ab') as file:
            print('writing binary')
            for i in self.convert_to_code():
                file.write(bytes(int(i)))

    def convert_to_code(self):
        """Function returns huffman coded text from plain text input."""
        code = '' #will cointain coded text
        #huff dict is {bitcode: character} keys, values need to be switched to encode
        huff_code_reverse = {char:code for code, char in self.huff_code.items()}

        #loop over all characters in text and add huffman code accordingly
        for char in self.content:
            code += huff_code_reverse[char]

        return code

    def convert_to_plain_text(self):
        """Function returns plain text from huffman coded text."""
        code = self.convert_to_code()
        text = '' #plain text to return
        part = '' #sequence to check if convertible to character

        #loop over all bits in coded text
        for i in code:
            if part in self.huff_code.keys():
                #if sequence if bits is in code-dict, add character to text
                text += self.huff_code[part]
                part = i #start new sequence
            else:
                #if not in dict, extend sequence
                part += i

        return text

    def savings(self):
        """Shows size savings if file is Huffman coded."""
        return '{:3.1f}% file size saved'.format( \
                (1-(len(self.convert_to_code())/(len(self.content)*8.0)))*100)

def test():
    t = Huff_Text('src/John Maynard.txt')
    print('content:')
    print(t.content)
    print('the resulting code:')
    print(t.convert_to_code())
    print('code converted back to text:')
    print(t.convert_to_plain_text())

if __name__ == '__main__':
    test()