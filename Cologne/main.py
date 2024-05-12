import Cologne

def example1():
    parser = Cologne.Parser(Cologne.ParserType.LALR_1)

    COLOGNE_START, COLOGNE_END = parser.get_default_symbols()

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
    parser = Cologne.Parser(Cologne.ParserType.LR_0)

    COLOGNE_START, COLOGNE_END = parser.get_default_symbols()

    NUMBER = parser.add_terminal(Cologne.Terminal("NUMBER"))
    PLUS = parser.add_terminal(Cologne.Terminal("PLUS"))
    MINUS = parser.add_terminal(Cologne.Terminal("MINUS"))

    expr = parser.add_non_terminal(Cologne.NonTerminal("expr"))

    parser.add_productions(
        Cologne.Production( expr, (expr, PLUS, expr) ),
        Cologne.Production( expr, (expr, MINUS, expr) ),
        Cologne.Production( expr, (NUMBER, ) )
    )

    parser.set_top_non_terminal(expr)

    return parser

parser = example1()
parser.generate_closures(debug=True)

# Generate the parse table
parse_table = Cologne.ParseTable(parser)
print(parse_table)
















