"""
# ----------------------------------------------------------------------
# clex.py
#
# A lexer for ANSI C.
# ----------------------------------------------------------------------
"""

def t_RPAREN(t):
    """
    \)
    """

    pass


def t_COMPONENT(t):
    """
    \.[xyz]
    """

    pass


def t_SEMI(t):
    """
    ;
    """

    pass


def t_CAPTURE(t):
    """
    `
    """

    pass


def t_COMMENT(t):
    """
    //.*
    """

    pass


def t_LBRACKET(t):
    """
    \[
    """

    pass


def t_LPAREN(t):
    """
    \(
    """

    pass


def t_COMMENT_BLOCK(t):
    """
    /\*(.|\n)*?\*/|/\*(.|\n)*?$
    """

    pass


def t_VAR(t):
    """
    \$[A-Za-z_][\w_]*
    """

    pass


def t_NEWLINE(t):
    """
    \n+|\r+
    """

    pass


def t_ID(t):
    """
    ([|]?([:]?([.]?[A-Za-z_][\w]*)+)+)+?
    """

    pass


def t_RBRACKET(t):
    """
    \]
    """

    pass


def t_ELLIPSIS(t):
    """
    \.\.
    """

    pass



t_MODEQUAL = '%='

t_TIMES = r'\*'

suspend_depth = 0

t_NOT = '!'

t_GE = '>='

t_PLUS = r'\+'

t_LVEC = '<<'

t_MINUSMINUS = '--'

t_ICONST = r'(0x[a-fA-F0-9]*)|\d+'

t_EQUALS = '='

t_MOD = '%'

t_CONDOP = r'\?'

t_TIMESEQUAL = r'\*='

t_CROSSEQUAL = '^='

t_LAND = '&&'

t_FCONST = r'(((\d+\.)(\d+)?|(\d+)?(\.\d+))(e(\+|-)?(\d+))?|(\d+)e(\+|-)?(\d+))([lL]|[fF])?'

id_state = None

t_GT = '>'

t_PLUSEQUAL = r'\+='

t_COLON = ':'

t_ignore = ' \t\x0c'

t_SCONST = r'"([^\\\n]|(\\.)|\\\n)*?"'

t_RBRACE = r'\}'

t_PLUSPLUS = r'\+\+'

t_LBRACE = r'\{'

reserved = ()

t_LT = '<'

t_DIVEQUAL = '/='

t_COMMA = ','

t_LE = '<='

t_EQ = '=='

t_MINUSEQUAL = '-='

t_DIVIDE = '/'

t_RVEC = '>>'

r = 'YES'

t_LOR = r'\|\|'

t_NE = '!='

t_CROSS = r'\^'

t_MINUS = '-'

tokens = ()

reserved_map = {}


