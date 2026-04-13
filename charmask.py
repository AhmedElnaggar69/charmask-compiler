import sys
from token import *
from lexer import *
if __name__ == '__main__':
    if len(sys.argv) != 2 :
        raise SystemExit('you have to use python3 charmask.py <filename>')
    filename = sys.argv[1]
    print(filename)

    with open(filename) as file:
        src = file.read()
        print(src)

        # todo (tokenize the src)
        tokens = lexer(src).tokenize()
        for tok in tokens:
            print(tok)
    