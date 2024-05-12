from Production import *

class ComplexProduction:
    def __init__(self, production, lookahead=None):
        """
        Creates a new ComplexProduction

        :param production: The simple production on which the complex production is based on
        :type production: Production

        :param lookahead: The lookahead token (Used only in LALR(1))
        :type lookahead: None if there is no lookahead, tuple otherwise.
        """

        self.result = production.result
        self.rule = production.rule
        self.cur_symbol = 0

        if lookahead == None:
            self.lookahead = tuple() # Create an empty tuple for the lookahead
        else:
            self.lookahead = lookahead

    def __str__(self):
        ret = f"{self.result} ->"
        dot_in_str = False

        for i, symbol in enumerate(self.rule):

            if i == self.cur_symbol:
                ret += " . " + str(symbol)
                dot_in_str = True
            else:
                ret += " " + str(symbol)
        
        if not dot_in_str:
            ret += f" ."
        
        if len(self.lookahead) != 0:
            ret += " (" + "/".join([str(symbol) for symbol in self.lookahead]) + ")"

        return ret

    def __eq__(self, other):
        if not isinstance(other, ComplexProduction):
            return False

        return self.rule == other.rule and self.result == other.result and self.cur_symbol == other.cur_symbol and self.lookahead == other.lookahead

    def __neq__(self, other):
        return not self == other
    
    def is_valid(self):
        """
        Checks whether the cur_symbol is still valid.

        :returns: Whether it is valid or not.
        :rtype: bool
        """

        return self.cur_symbol <= len(self.rule)

    def can_generate_more(self):
        """
        Checks whether or not this production can be used to generate more productions

        :returns: True if yes, False if no.
        :rtype: bool
        """

        return self.cur_symbol < len(self.rule)

    def get_prev_symbol(self):
        """
        Returns the previous symbol.

        :returns: the previous symbol
        :rtype: ParserSymbol
        """

        return self.rule[self.cur_symbol - 1]

    def get_current_symbol(self):
        """
        Returns the current symbol.

        :returns: the previous symbol
        :rtype: ParserSymbol
        """
        return self.rule[self.cur_symbol]

    def get_prod_next_symbol(self):
        """
        Makes a production with the next symbol

        :returns: This production with the next symbol
        :rtype: ComplexProduction
        """
        ret = ComplexProduction(self.get_simple_production())

        if self.cur_symbol < len(self.rule):
            ret.cur_symbol = self.cur_symbol + 1
        else:
            ret.cur_symbol = self.cur_symbol

        return ret
        
    def get_simple_production(self):
        """
        Returns the simple production of this production (Without cur_symbol)

        :returns: The simple production
        :rtype: Production
        """

        return Production(self.result, self.rule)

    def advance(self):
        """
        Advances the cur_symbol by one.
        
        :returns: Nothing
        :rtype: None
        """
        if self.cur_symbol < len(self.rule):
            self.cur_symbol += 1

    def get_derived_lookaheads(self, parser):
        """
        Gets the derived lookahead symbols for hte proudctions derived from this production.

        :param parser: The parser from which the productions and closures are generated.
        :type parser: Parser

        :returns: The lookahead symbols
        """
        
        return ""





