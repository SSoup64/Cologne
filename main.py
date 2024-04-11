"""
import Cologne

parser = Cologne.Parser()

COLOGNE_START, COLOGNE_END = parser.get_default_terminals()

a = parser.add_terminal(Cologne.Terminal("a"))
b = parser.add_terminal(Cologne.Terminal("b"))

A = parser.add_non_terminal(Cologne.NonTerminal("A"))
S = parser.add_non_terminal(Cologne.NonTerminal("S"))

parser.add_production(
    Cologne.Production( S, (A, A) )
)

parser.add_production(
    Cologne.Production( A, (a, A) )
)

parser.add_production(
    Cologne.Production( A, (b, ) )
)

parser.set_top_non_termianl(S)

parser.parse(debug=True)
"""

import Cologne

parser = Cologne.Parser()

COLOGNE_START, COLOGNE_END = parser.get_default_terminals()

NUMBER = parser.add_terminal(Cologne.Terminal("NUMBER"))
PLUS = parser.add_terminal(Cologne.Terminal("PLUS"))
MINUS = parser.add_terminal(Cologne.Terminal("MINUS"))
TIMES = parser.add_terminal(Cologne.Terminal("TIMES"))
DIVIDE = parser.add_terminal(Cologne.Terminal("DIVIDE"))

expr = parser.add_non_terminal(Cologne.NonTerminal("expr"))

parser.add_production(
    Cologne.Production( expr, (expr, PLUS, expr) )
)
parser.add_production(
    Cologne.Production( expr, (expr, MINUS, expr) )
)
parser.add_production(
    Cologne.Production( expr, (expr, TIMES, expr) )
)
parser.add_production(
    Cologne.Production( expr, (expr, DIVIDE, expr) )
)
parser.add_production(
    Cologne.Production( expr, (NUMBER, ) )
)

parser.set_top_non_terminal(expr)
parser.parse(debug=True)



