"""
The tokenizer should read in a stream of legal tokens from the given input file and produce a corresponding
stream of numbers corresponding to the tokens, one number per line, as its output
author: Lily Driscoll.169
"""
import sys

RW = {"program": 1, "begin": 2, "end": 3, "int": 4, "if": 5, "then": 6, "else": 7, "while": 8, "loop": 9,
      "read": 10,
      "write": 11, "eof": 33}
SS = {";": 12, ",": 13, "=": 14, "!": 15, "[": 16, "]": 17, "&&": 18, "||": 19, "(": 20, ")": 21, "+": 22, "-": 23,
      "*": 24, "!=": 25, "==": 26, "<": 27, ">": 28, "<=": 29, ">=": 30}
GT = ["!", "=", "<", ">"]


class Tokenizer:

    def __init__(self, file):
        self.file = file
        self.currLiteral = ""
        self.currToken = -1
        self.tokens = []
        self.token_literals = []
        self.index = 0

    def getToken(self):  # returns (info about) current  token
        if self.currLiteral in RW.keys():
            self.currToken = RW.get(self.currLiteral)
        elif self.currLiteral in SS.keys():
            self.currToken = SS.get(self.currLiteral)
        elif self.currLiteral[0].isupper():
            for x in self.currLiteral:
                if x.islower():
                    print("Identifier detected with lowercase, not allowed")
                    sys.exit(1)
            self.currToken = 32
        elif self.currLiteral.isdigit():
            self.currToken = 31
        self.tokens.append(self.currToken)
        return self.currToken

    def skipToken(self):  # skips current token, next token becomes current token
        self.index += 1
        self.currLiteral = self.token_literals[self.index]

    def intVal(self):  # returns the value of the current (integer) token
        return self.currLiteral

    def idName(self):  # returns the name (String) of the current (id) token
        return self.currLiteral

    def tokenize(self):
        try:
            f = open(self.file, "r")
        except FileNotFoundError:
            print("File not found, refer to ReadMe.txt for more help")
            sys.exit(1)
        skip = -1
        currToken = ""
        for line in f:  # Generates a list of words from the text file
            for x in range(len(line)):
                if x == skip:
                    continue
                if line[x].isspace() and len(currToken) > 0:
                    self.token_literals.append(currToken.strip())
                    currToken = ""
                elif line[x] in SS:
                    if line[x:x + 2] in SS:
                        if len(currToken) > 0:
                            self.token_literals.append(currToken.strip())
                        currToken = line[x]
                        x += 1
                        currToken += line[x]
                        self.token_literals.append(currToken)
                        currToken = ""
                        skip = x
                    elif len(currToken) > 0:
                        self.token_literals.append(currToken.strip())
                        self.token_literals.append(line[x])
                        currToken = ""
                    else:
                        self.token_literals.append(line[x])
                else:
                    currToken = currToken + line[x]
        self.token_literals.append(currToken)
        self.token_literals.append("eof")
        while "" in self.token_literals:
            self.token_literals.remove("")


if __name__ == "__main__":
    try:
        tk = Tokenizer(sys.argv[1])
        output = open(sys.argv[2], "w")
    except IndexError:
        print("Not enough arguments given, see ReadMe.txt for more information")
        sys.exit(1)
    tk.tokenize()

    tk.currLiteral = tk.token_literals[0]
    while tk.getToken() != 33:
        print(tk.getToken())
        output.write(tk.getToken())
        tk.skipToken()
    print(tk.getToken())
