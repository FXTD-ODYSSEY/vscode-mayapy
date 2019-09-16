"""
# ----------------------------------------------------------------------
# ctokens.py
#
# Token specifications for symbols in ANSI C and C++.  This file is
# meant to be used as a library in other tokenizers.
# ----------------------------------------------------------------------
"""

def t_CPPCOMMENT(t):
    """
    //.*\n
    """

    pass


def t_COMMENT(t):
    """
    /\*(.|\n)*?\*/
    """

    pass



t_TIMESEQUAL = r'\*='

t_ANDEQUAL = '&='

t_LSHIFTEQUAL = '<<='

t_LNOT = '!'

t_LE = '<='

t_INTEGER = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

t_TERNARY = r'\?'

t_OR = r'\|'

t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

t_XOR = r'\^'

t_LBRACKET = r'\['

t_INCREMENT = r'\+\+'

t_OREQUAL = r'\|='

t_MODULO = '%'

t_ID = '[A-Za-z_][A-Za-z0-9_]*'

t_PLUSEQUAL = r'\+='

t_GT = '>'

t_RSHIFT = '>>'

t_RPAREN = r'\)'

t_MODEQUAL = '%='

t_STRING = r'\"([^\\\n]|(\\.))*?\"'

t_EQUALS = '='

t_LSHIFT = '<<'

t_PLUS = r'\+'

t_COLON = ':'

t_RSHIFTEQUAL = '>>='

t_AND = '&'

t_SEMI = ';'

t_LBRACE = r'\{'

t_LPAREN = r'\('

t_MINUSEQUAL = '-='

t_LOR = r'\|\|'

t_RBRACE = r'\}'

t_ELLIPSIS = r'\.\.\.'

t_LT = '<'

t_XOREQUAL = '^='

t_ARROW = '->'

t_NE = '!='

t_COMMA = ','

t_EQ = '=='

t_MINUS = '-'

t_RBRACKET = r'\]'

t_DIVEQUAL = '/='

t_TIMES = r'\*'

t_DIVIDE = '/'

t_DECREMENT = '--'

t_PERIOD = r'\.'

t_LAND = '&&'

tokens = []

t_NOT = '~'

t_CHARACTER = r"(L)?\'([^\\\n]|(\\.))*?\'"

t_GE = '>='


