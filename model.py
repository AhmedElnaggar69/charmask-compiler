class Expr:
    # exp -> (x+3) > (t+r)
    pass

class Stmt:
    # statements preforms actions
    pass

class Integer(Expr):

    def __init__(self , tok):
        assert isinstance(tok , int) , f"assertion failure -> {tok}"
        self.tok = tok

    def __repr__(self , tok):
        return f"INTEGER -> [ {tok} ]"


class Float(Expr):
    def __init__(self , tok):
        assert isinstance(tok , float) , f"assertion failure -> {tok}"
        self.tok = tok

    def __repr__(self , tok):
        return f"FLOAT -> [ {tok} ]"

class BinOp(Expr):
    def __init__(self , op:Token , rhs:Expr , lhs:Expr ):
        assert isinstance(op , Token) , f"assertion failure -> {op}"
        assert isinstance(rhs , Expr) , f"assertion failure -> {rhs}"        
        assert isinstance(lhs , Expr) , f"assertion failure -> {lhs}"

        self.op = op
        self.rhs = rhs
        self.lhs = lhs
    def __repr__(self):
        return f"binop : {self.op.lexeme!r} , {self.lhs} , {self.rhs}"

class Unop(Expr):
    def __init__(self ,op:Token ,  operand:Expr):
        assert isinstance(op , Token) , f"assertion failure -> {op}"
        assert isinstance(oprand , Expr) , f"assertion failure -> {oprand}"
        
        self.op = op
        self.oprand
    def __repr__(self):
        return f"uinop : {self.op.lexeme!r} , {self.oprand}"



class WhileStmt(Stmt):
    pass


class Assignement(Stmt):
    pass

class Grouping(Expr):
    # exp : ( <expr> )
    def __init__(self , tok):
        assert isinstance(tok , Expr) , f"assertion failure -> {tok}"
        self.tok = tok

    def __repr__(self , tok):
        return f"Grouping -> {tok}"