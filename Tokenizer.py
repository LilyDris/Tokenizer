"""The tokenizer should read in a stream of legal tokens from the given input file and produce a corresponding
stream of numbers corresponding to the tokens, one number per line, as its output"""
import sys


RW= {"program":1,"begin":2,"end":3,"int":4,"if":5,"then":6,"else":7,"while":8,"loop":9,"read":10,"write":11, "eof":33}
SS={";":12,",":13,"=":14,"!":15,"[":16,"]":17,"&&":18,"||":19,"(":20,")":21,"+":22,"-":23,"*":24,"!=":25,"==":26,"<":27,">":28,"<=":29,">=":30}

def getToken(token):  #returns (info about) current  token
    key=-1
    if(token in RW.keys()):
        key=RW.get(token)
    elif(token in SS.keys()):
        key=SS.get(token)
    elif(token[0].isupper()):
        for x in token:
            if x.islower():
                print("Indetifier detected with lowercase, not allowed")
                sys.exit(1)
        key=32
    elif(token[0].isdigit()):
        key=31
    return key
    

def skipToken():  #skips current token, next token becomes current token
    y=0
    
    
def intVal():  #returns the value of the current (integer) token
    return 0


def idName(): # returns the name (String) of the current (id) token
    idName=""
    return idName


def main(argv):
    currToken=""
    tokenList=[]
    document=""
    try:
        document= argv[1]
    except IndexError:
        print("No argument given, see ReadMe.txt for more information")
        sys.exit(1)

    try:
        f=open(document,"r")
    except FileNotFoundError:
        print("File not found, refer to ReadMe.txt for more help")
        sys.exit(1)
    
    skip=-1
    for line in f:  #Generates a list of words from the text file
        for x in range(len(line)):
            if x==skip:
                continue
            if(line[x].isspace() and len(currToken)>0):
                tokenList.append(currToken.strip())
                currToken=""
            elif(line[x] in SS):
                if line[x:x+2] in SS:
                    if(len(currToken)>0):
                        tokenList.append(currToken.strip())
                    currToken=line[x]
                    x+=1
                    currToken+=line[x]
                    tokenList.append(currToken)
                    currToken=""
                    skip=x
                elif(len(currToken)>0):
                    tokenList.append(currToken.strip())
                    tokenList.append(line[x])
                    currToken=""
                else:
                    tokenList.append(line[x])
            else:
                currToken=currToken+line[x]
    tokenList.append(currToken)
    tokenList.append("eof")
    while("" in tokenList):
        tokenList.remove("")
    print(tokenList)
    
    for token in tokenList:
        print(getToken(token.strip()))
     

    return 0


if __name__ == "__main__":
    main(sys.argv)