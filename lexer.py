from token import *
numsContainer = ['0','1','2','3','4','5','6','7','8','9']
KEYWORDS = [
    "if",
    "then",
    "else",
    "true",
    "false",
    "and",
    "or",
    "while",
    "do",
    "for",
    "func",
    "null",
    "end",
    "print",
    "println",
    "return"
]
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
            
            # todo (ints and float parser)
            self.NumberTokenizer(char=char)
            self.stringParser(char=char , sign='"')
            self.stringParser(char=char , sign="'")
            self.IdParser(char=char)
            # todo : check if it starts with "" or '' and get the string token
            # todo : apha chars (a letter) or identifier

        return self.tokens
    

    def NumberTokenizer(self,char):
        if char in numsContainer:
            while self.look() in numsContainer:
                self.advance();
                if self.look() == '.' and self.look_forward() in numsContainer:
                    self.advance()
                    while self.look() in numsContainer:
                        self.advance();
                    self.add_token(TOK_FLOAT)
                else:
                    self.add_token(TOK_INTEGER)
    def IdParser(self , char):
        if char.isalpha() or char=='_':
            while self.curr < len(self.src) and ( self.look().isalnum() or self.look() == '_' ):
                self.advance()
            subString = self.src[self.start:self.curr]
            if subString in KEYWORDS:
                print("working")
                if subString == "if":
                    self.add_token(TOK_IF)
                elif subString == "then":
                    self.add_token(TOK_THEN)
                elif subString == "else":
                    self.add_token(TOK_ELSE)
                elif subString == "true":
                    self.add_token(TOK_TRUE)
                elif subString == "false":
                    self.add_token(TOK_FALSE)
                elif subString == "and":
                    self.add_token(TOK_AND)
                elif subString == "or":
                    self.add_token(TOK_OR)
                elif subString == "while":
                    self.add_token(TOK_WHILE)
                elif subString == "do":
                    self.add_token(TOK_DO)
                elif subString == "for":
                    self.add_token(TOK_FOR)
                elif subString == "func":
                    self.add_token(TOK_FUNC)
                elif subString == "null":
                    self.add_token(TOK_NULL)
                elif subString == "end":
                    self.add_token(TOK_END)
                elif subString == "print":
                    self.add_token(TOK_PRINT)
                elif subString == "println":
                    self.add_token(TOK_PRINTLN)
                elif subString == "return":
                    self.add_token(TOK_RET)
            else:
                self.add_token(TOK_IDENTIFIER)
    
    def stringParser(self , char , sign):
        if char==sign:
            self.start = self.curr
            while self.look() != sign and not self.curr >= len(self.src):
               self.advance();
            

            # if we reached the end of the src file scaning for the end of the string without finding the closing '/"
            if self.curr >= len(self.src):
                raise SystemError("reached the end of the file scaning for a closing sign for a string")
            

            self.add_token(TOK_STRING)
            self.advance();
      

    def advance(self):
        if self.curr >= len(self.src):
            return False
        
        
        char = self.src[self.curr]
        self.curr = self.curr + 1
        return char
    

    def look(self):
        if self.curr >= len(self.src):
            return False
        
        return self.src[self.curr]
    
    
    def look_forward(self , n=1):
        if self.curr + 1 >= len(self.src):
            return False
        
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

