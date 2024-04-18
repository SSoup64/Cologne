# Pandas is used for the str representation of the parse table
import pandas as pd

from TableAction import *

class ParseTable:
    def __init__(self, parser):
        """
        Creates a parse table from a parser object.
        
        :param parser: The parser to generate the table from
        :type parser: Parser
        """
        
        if not parser.closures:
            raise Exception("Tried to generate a parse table from a parser with no closures. Did you forget to call 'parser.generate_closures'?")

        # There are closures generated
        self.productions = tuple(parser.productions)
        self.parser = parser

        # The table shall be a dictionart that matches a Symbol to a list of integers.
        self.table = {}

        self.__generate_table()

    def __str__(self):
        return str(pd.DataFrame(self.table))
    
    def __generate_table(self):
        """
        Actually generates the table from the data.

        :returns: Nothing
        :rtype: None
        """

        COLOGNE_START, COLOGNE_END = self.parser.get_default_terminals()

        # Create the base list (Where everything is an error).
        base_column = [TableAction(TableActionType.ERROR, 0)] * len(self.parser.closures)
        
        # Add the terminals
        for terminal in self.parser.terminals:
            if terminal != COLOGNE_START:
                self.table.update({terminal: base_column.copy()})

        # Add the non terminals
        for non_terminal in self.parser.non_terminals:
            self.table.update({non_terminal: base_column.copy()})

        # Generate the actions
        for closure_index, closure in enumerate(self.parser.closures):
            if closure.goto:
                # The closure is not a final closure

                for goto_symbol, goto_closure in closure.goto.items():
                    self.table[goto_symbol][closure_index] = TableAction(TableActionType.SHIFT, goto_closure)
            else:
                # The closure is a final closure
                # Since it is a final closure, it only has one production
                final_production = closure.complex_productions[0]

                if final_production.result == COLOGNE_START:
                    # We have gotten to the starting production.
                    # Therefore, we can accept
                    self.table[COLOGNE_END][closure_index] = TableAction(TableActionType.ACCEPT, 0)
                else:
                    # We should reduce it.

                    # Find the index of the final production
                    final_production_index = self.productions.index(final_production.get_simple_production())

                    # Since right now, the only parser available is LR(0), I am going to hardcode the behavior here.
                    for key in self.table.keys():
                        if key in self.parser.terminals:
                            self.table[key][closure_index] = TableAction(TableActionType(TableActionType.REDUCE), final_production_index)















