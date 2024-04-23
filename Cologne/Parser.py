from NonTerminal import *
from Terminal import *
from Production import *
from Closure import *
from ParserType import *

NON_TERMINAL_COLOGNE_START_INDEX = 0
TERMINAL_COLOGNE_END_INDEX = 0

class Parser:
    def __init__(self, parser_type):
        """
        Creates a new parser object

        :param parser_type: Indicates whether the parser is LR(0) or LALR(1).
        :type parser_type: ParserType.
        """

        self.top_non_terminal = None

        self.preps_done = False

        self.parser_type = parser_type

        self.non_terminals = [NonTerminal("COLOGNE_START")]
        self.terminals = [Terminal("COLOGNE_END")]
        self.productions = []
        self.closures = []
        self.lookaheads = {} # Basically, if we want to find the lookhead of a production based on nonterminal, this is gonna be the list of the lookaheads
    
    def __str__(self):
        """
        Creates the string representation of a parser object.

        :returns: The string representation of the parser object (Includes the terminals, non terminals and productions).
        :rtype: str
        """

        ret = ""
        
        # Terminals
        ret += "Terminals:"
        
        for terminal in self.terminals:
            ret += "\n" + str(terminal)

        ret += "\n\n"

        # Non terminals
        ret += "Non terminals:"
        
        for non_terminal in self.non_terminals:
            ret += "\n" + str(non_terminal)
        
        ret += "\n\n"

        # Productions
        ret += "Productions:"

        for production in self.productions:
            ret += "\n" + str(production)

        return ret

    def add_terminal(self, terminal):
        """
        Adds a terminal to the list of valid terminals

        :param terminal: The terminal to add
        :type terminal: Terminal

        :returns: The terminal added
        :rtype: Terminal
        """
        
        if isinstance(terminal, Terminal) and terminal not in self.terminals:
            self.terminals.append(terminal)
            return terminal
        
        return None

    def add_non_terminal(self, non_terminal):
        """
        Adds a non terminal to the list of valid non terminals

        :param non terminal: The terminal to add
        :type non terminal: NonTerminal

        :returns: The non terminal added
        :rtype: NonTerminal
        """
        
        if isinstance(non_terminal, NonTerminal) and non_terminal not in self.non_terminals:
            self.non_terminals.append(non_terminal)
            return non_terminal
        
        return None

    def add_production(self, production):
        """
        Adds a production to the list of valid productions

        :param production: The production to add.
        :type production: Production

        :returns: Nothing.
        :rtype: None
        """

        if isinstance(production, Production) and production not in self.productions:
            self.productions.append(production)

        return None

    def add_productions(self, *argv):
        """
        Adds a number of productions at the same time to the parser.

        :param *argv: The productions
        :type *argv: list

        :returns: Nothing.
        :rtype: None
        """

        for production in argv:
            self.add_production(production)

    def __create_closures(self):
        """
        Generates the closures from the productions

        :returns: Nothing
        :rtype: None
        """

        COLOGNE_START, COLOGNE_END = self.get_default_symbols()
        first_closure = Closure()

        if self.parser_type == ParserType.LALR_1:
            base_production_first_closure = ComplexProduction(self.productions[-1], (COLOGNE_END, ));
            pass
        elif self.parser_type == ParserType.LR_0:
            base_production_first_closure = ComplexProduction(self.productions[-1]);

        first_closure.create_productions(base_production_first_closure, self)
        
        self.closures.append(first_closure)

        self.closures[-1].generate_next_closures(self.closures, selfs)
    
    def generate_closures(self, debug=False):
        """
        Generates the parsing table from the productions

        :param debug: Whether or not to print debug info
        :type Debug: bool
        """

        self.__preparsing()

        print("Generating closures...")
        
        self.__create_closures()

        if debug:
            print("Closures:")

            for ind, closure in enumerate(self.closures):
                print(f"{ind}. {closure}")
    
    def get_default_symbols(self):
        """
        Returns the two default terminals that the parser creates: COLONGE_START, COLOGNE_END

        :returns: the two default terminals that the parser creates.
        :rtype: tuple
        """
        
        return self.non_terminals[NON_TERMINAL_COLOGNE_START_INDEX], self.terminals[TERMINAL_COLOGNE_END_INDEX]
    
    def set_top_non_terminal(self, non_terminal):
        """
        Sets the top most non-terminal.

        :param non_terminal: The top most non terminal.
        :type non_terminal: NonTerminal

        :returns: Nothing
        :rtype: None
        """

        if isinstance(non_terminal, NonTerminal):
            self.top_non_terminal = non_terminal

    def __preparsing(self):
        """
        Sets up some stuff for the parsing itself
        
        :returns: Nothing.
        :rtype: None
        """
        
        if not self.preps_done:
            # Add the starting production (S' -> S)
            if self.top_non_terminal == None:
                raise Exception("top_non_terminal not set. Did you forget to call 'parser.set_top_non_terminal'?")
            
            self.add_production(Production(self.non_terminals[NON_TERMINAL_COLOGNE_START_INDEX], (self.top_non_terminal, )))
            
            if self.parser_type == ParserType.LALR_1:
                # TODO: Make sure that the generated symbols are only terminals
                # Generate the possible lookaheads for all non terminals
                print("Generating the possible lookaheads for non terminals...")

                for symbol in self.non_terminals:
                    this_lookahead = []

                    for production in self.productions:

                        if production.result == symbol:
                            this_lookahead.append(production.rule[0])

                    self.lookaheads.update({symbol: tuple(this_lookahead)})












