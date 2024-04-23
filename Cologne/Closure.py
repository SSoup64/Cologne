from ComplexProduction import *
from ParserType import *

CLOSURE_PRINT_TAB = "    "

class Closure:
    def __init__(self):
        self.complex_productions = []
        self.goto = {}
        self.productions_checked = []

    def __str__(self):
        ret = "Closure {\n"

        for production in self.complex_productions:
            ret += CLOSURE_PRINT_TAB + str(production) + "\n"

        ret += "\n"

        for key, val in self.goto.items():
            ret += CLOSURE_PRINT_TAB + f"{key}: {val}\n"

        ret += "}"

        return ret

    def __eq__(self, other):
        if not isinstance(other, Closure):
            return False

        if len(other.complex_productions) != len(self.complex_productions):
            return False

        for i in range(len(self.complex_productions)):
            if self.complex_productions[i] != other.complex_productions[i]:
                return False

        return True

    def __ne__(self, other):
        return not self == other

    def create_productions(self, base_production, parser):
        """
        Generates the complex productions for this closure

        :param base_production: The base production in which this closure is based on
        :type base_production: ComplexProduction

        :param parser: The parser from which we generate the other productions
        :type parser: Parser

        :returns: Nothing
        :rtype: None
        """
        
        self.__create_productions_recursion(base_production, parser)

    def __create_productions_recursion(self, base_production, parser):
        """
        Generates the complex productions from a base production.

        :param base_production: The base production in which this closure is based on
        :type base_production: ComplexProduction

        :param parser: The parser from which we generate the other productions
        :type parser: Parser

        :returns: Nothing
        :rtype: None
        """
        
        self.complex_productions.append(base_production)
        
        productions_lookaheads = base_production.get_derived_lookaheads(parser)

        if base_production.can_generate_more():
            symbol = base_production.get_current_symbol()

            for production in parser.productions:
                if production.result == symbol and production not in self.productions_checked:
                    # TODO implement the lookahead
                    self.productions_checked.append(production)
                    self.__create_productions_recursion(ComplexProduction(production), parser)

    def generate_next_closures(self, closures, parser):
        """
        Generates the next closures from the current closure.

        :param closures: A list of all the previous closures
        :type closures: list
        
        :param parser: The parser from which we generate the closures
        :type parser: Parser

        :returns: Nothing
        :rtype: None
        """
        
        for my_production in self.complex_productions:
            next_closure_index = 0
            
            new_closure = Closure()

            production = my_production.get_prod_next_symbol()

            if production.is_valid():
                new_closure.create_productions(production, parser)
                
                # if check_closure_in_list(new_closure, closures) == False:
                if new_closure not in closures:
                    closures.append(new_closure)
                    next_closure_index = len(closures) - 1

                    closures[-1].generate_next_closures(closures, parser)
                else:
                    next_closure_index = closures.index(new_closure)
                
                # Check if all the productions in this production are final
                cant_add = True

                for complex_production in self.complex_productions:
                    if complex_production.can_generate_more():
                        cant_add = False
                
                if not cant_add:
                    self.goto[production.get_prev_symbol()] = next_closure_index




