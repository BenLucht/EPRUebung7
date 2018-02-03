"""
Tree module, implements a tree class for making Huffman codes.
"""

__author__ = "4897491: Benjamin Lucht, 2188645: Anne Schwarz"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "We would like to thank our coffee for the morning motivation."
__email__ = "9047212@stud.uni-frankfurt.de, anne@frauschwarz.org"

import random

class Node():
    """Implements nodes of a tree."""

    def __init__(self, character=None, nodes=None, weight=0):
        """
        Makes new Node for a tree.
        If character and weight given makes a simple node,
        if sub-nodes given, makes a new subtree with the nodes.
        """
        self.character = character
        self.nodes = nodes
        self.weight = weight
        self.previous = None #for easier tree navigation
        if self.nodes:
            self.character = ''
            for node in nodes:
                self.character += node.character
                self.weight += node.weight
                node.previous = self

class Tree_Maker():
    """Tree_Maker implements methods to make a tree for Huffman coding."""

    def __init__(self, nodes):
        self.nodes = nodes
        self.tree = self.make_huff()

    def make_huff(self):
        """Implements the Huffman tree algorithm from lecture slides."""

        ordered_by_weight = self.nodes

        while len(ordered_by_weight) >= 2:
            #custom sort by weights
            ordered_by_weight = sorted(ordered_by_weight, key=lambda node: node.weight)
            one = ordered_by_weight.pop(0) #left tree arm
            two = ordered_by_weight.pop(0) #right tree arm
            #puts new subtree back into node list
            ordered_by_weight.append(Node(nodes=[one, two]))

        return ordered_by_weight[0]

    def make_dict(self):
        """Makes dictionary {code:character} from tree."""

        char_dict = {}

        #goes through all initial nodes to find their path to root
        for node in self.nodes:
            node_char = node.character
            path = ''
            while node.previous != None:
                path = str(node.previous.nodes.index(node)) + path
                node = node.previous
            char_dict[path] = node_char
        return char_dict

def test():
    chars = 'abcdefghi'
    nodes = []
    for char in chars:
        nodes.append(Node(character=char, weight=random.randint(1,9)))
    for node in nodes:
        print(node.character, node.weight)

    maker = Tree_Maker(nodes)
    d = maker.make_dict()
    print(d)

if __name__ == '__main__':
    test()