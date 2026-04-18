from token import *
from model import *
class parser:
    def __init__(self,tokens):
        tokens = self.tokens
        curr = 0
    def parse(self):
        ast = self.expr()
        return ast
    def primary(self):
        pass
    def unary(self):
        pass
    def term(self):
        pass
    def expr(self):
        pass
    def factor(self):
        pass