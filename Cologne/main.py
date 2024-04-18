import Cologne

def example1():
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

    parser.set_top_non_terminal(S)

    return parser

def example2():
    parser = Cologne.Parser()

    COLOGNE_START, COLOGNE_END = parser.get_default_terminals()

    NUMBER = parser.add_terminal(Cologne.Terminal("NUMBER"))
    PLUS = parser.add_terminal(Cologne.Terminal("PLUS"))
    MINUS = parser.add_terminal(Cologne.Terminal("MINUS"))
    TIMES = parser.add_terminal(Cologne.Terminal("TIMES"))
    DIVIDE = parser.add_terminal(Cologne.Terminal("DIVIDE"))

    expr = parser.add_non_terminal(Cologne.NonTerminal("expr"))


    parser.add_productions(
        Cologne.Production( expr, (expr, PLUS, expr) ),
        Cologne.Production( expr, (expr, MINUS, expr) ),
        Cologne.Production( expr, (expr, TIMES, expr) ),
        Cologne.Production( expr, (expr, DIVIDE, expr) ),
        Cologne.Production( expr, (NUMBER, ) )
    )

    parser.set_top_non_terminal(expr)

    return parser

parser = example2()
parser.generate_closures(debug=True)

# Generate the parse table
parse_table = Cologne.ParseTable(parser)
print(parse_table)
















