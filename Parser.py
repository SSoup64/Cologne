from NonTerminal import *
from Terminal import *
from Production import *
from Closure import *

TERMINAL_COLOGNE_START_INDEX = 0
TERMINAL_COLOGNE_END_INDEX = 1

class Parser:
    def __init__(self):
        self.non_terminals = []
        self.terminals = [Terminal("COLOGNE_START"), Terminal("COLOGNE_END")]
        self.productions = []
        self.closures = []

        self.preps_done = False
        self.top_non_terminal = None
    
    def __str__(self):
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

    def __create_closures(self):
        first_closure = Closure()
        # first_closure.create_productions(ComplexProduction(self.productions[-1], self.terminals), self.productions)
        first_closure.create_productions(ComplexProduction(self.productions[-1]), self.productions)
        
        self.closures.append(first_closure)

        self.closures[-1].generate_next_closures(self.closures, self.productions)
    
    def parse(self, debug=False):
        self.__preparsing()

        print("Generating closures...")
        
        self.__create_closures()

        if debug:
            print("Closures:")

            for ind, closure in enumerate(self.closures):
                print(f"{ind}. {closure}")
    
    def get_default_terminals(self):
        """
        Returns the two default terminals that the parser creates: COLONGE_START, COLOGNE_END

        :returns: the two default terminals that the parser creates.
        :rtype: tuple
        """
        
        return self.terminals[TERMINAL_COLOGNE_START_INDEX], self.terminals[TERMINAL_COLOGNE_END_INDEX]
    
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
            
            self.add_production(Production(self.terminals[TERMINAL_COLOGNE_START_INDEX], (self.top_non_terminal, )))



