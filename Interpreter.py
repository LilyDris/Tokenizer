"""
Your interpreter should take two command-line arguments. The first will be the name of the file that
contains the Core program to be interpreted. The second will be the name of the file that contains the
data for the Core program.
author: Lily Driscoll.169
"""
from main import Tokenizer
import sys


class Leaf:

    def __init__(self, id_no, alt_no, name):
        self.id = id_no
        self.altNo = alt_no
        self.name = name
        self.parent = None
        self.child = []

    def create_child(self, id_no, alt_no, name):
        self.child.append(Leaf(id_no, alt_no, name))
        self.child[-1].parent = self
