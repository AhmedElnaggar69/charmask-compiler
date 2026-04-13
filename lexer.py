from token import *
class lexer:
    def __init__(self , src):
        self.tokens = []
        self.curr = 0 
        self.start = 0
        self.src = src
        self.line = 1

    def add_token(self , tokenType):
        self.tokens.append(token(tokenType , self.src[self.start:self.curr] , self.line))
    def tokenize(self):
        # scan tokens from the src and add them to the list
        while(self.curr < len(self.src)):
            self.start = self.curr
            char = self.advance()

            if char == '\n':
                self.line = self.line + 1
            elif char == '\t':
                pass
            elif char == '\r':
                pass
            elif char == ' ':
                pass
            elif char == '$':
                while self.look() != '\n' and not self.curr >= len(self.src):
                    self.advance()
            elif char == '+':
                self.add_token(TOK_PLUS)

            elif char == '-':
                self.add_token(TOK_MINUS)

            elif char == '*':
                self.add_token(TOK_STAR)

            elif char == '/':
                self.add_token(TOK_SLASH)

            elif char == '^':
                self.add_token(TOK_CARET)

            elif char == '%':
                self.add_token(TOK_MOD)

            elif char == '(':
                self.add_token(TOK_LPAREN)

            elif char == ')':
                self.add_token(TOK_RPAREN)

            elif char == '{':
                self.add_token(TOK_LCURLY)

            elif char == '}':
                self.add_token(TOK_RCURLY)

            elif char == '[':
                self.add_token(TOK_LSQUAR)

            elif char == ']':
                self.add_token(TOK_RSQUAR)

            elif char == ',':
                self.add_token(TOK_COMMA)

            elif char == '.':
                self.add_token(TOK_DOT)

            elif char == ':':
                self.add_token(TOK_COLON)

            elif char == ';':
                self.add_token(TOK_SEMICOLON)

            elif char == '?':
                self.add_token(TOK_QUESTION)

            elif char == '=':
                if self.match('='):
                    self.add_token(TOK_EQ)
                else:
                    self.add_token(TOK_ASSIGN)

            elif char == '!':
                if self.match('='):
                    self.add_token(TOK_NE)
                else :
                    self.add_token(TOK_NOT)


            elif char == '>':
                if self.match('='):
                    self.add_token(TOK_GE)
                elif self.match('>'):
                    self.add_token(TOK_GTGT)
                else:
                    self.add_token(TOK_GT)



            elif char == '<':
                if self.match('='):
                    self.add_token(TOK_LE)
                elif self.match('<'):
                    self.add_token(TOK_LTLT)
                else:
                    self.add_token(TOK_LT)


            # todo : (check numarical) and do logic for ints and floats
            # todo : check if it starts with "" or '' and get the string token
            # todo : apha chars (a letter) or identifier

        return self.tokens
    
    def advance(self):
        char = self.src[self.curr]
        self.curr = self.curr + 1
        return char
    

    def look(self):
        return self.src[self.curr]
    
    
    def look_forward(self , n=1):
        if self.curr >= len(self.src):
            return '\0'
        return self.src[self.curr + n]
    
    
    def match(self , expected):
        if self.curr >= len(self.src):
            return False
        if self.src[self.curr] != expected:
            return False
        self.curr = self.curr + 1
        return True

