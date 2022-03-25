from main import Tokenizer
import sys


class Leaf:
    # Parse tree init
    def __init__(self, id_no, alt_no, name):
        self.id = id_no
        self.altNo = alt_no
        self.name = name
        self.parent = None
        self.child = []

    # Adds leaf node
    def create_child(self, id_no, alt_no, name):
        self.child.append(Leaf(id_no, alt_no, name))
        self.child[-1].parent = self


# Parser
class ParseTree:

    # initialize pt
    def __init__(self, id_no):
        self.tokens = {}
        self.declare = True
        self.token = id_no
        self.root = Leaf(0, 0, "<program>")
        self.parse()


