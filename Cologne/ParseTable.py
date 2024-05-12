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
        ret = ""
        
        for production_index, production in enumerate(self.productions):
            ret += f"{production_index}. {production}\n"
        
        ret += str(pd.DataFrame(self.table))
        
        return ret
    
    def __generate_table(self):
        """
        Actually generates the table from the data.

        :returns: Nothing
        :rtype: None
        """

        COLOGNE_START, COLOGNE_END = self.parser.get_default_symbols()

        # Create the base list (Where everything is an error).
        base_column = [TableAction(TableActionType.ERROR, 0)] * len(self.parser.closures)
        
        # Add the terminals
        for terminal in self.parser.terminals:
            self.table.update({terminal: base_column.copy()})

        # Add the non terminals
        for non_terminal in self.parser.non_terminals:
            # Don't include the COLOGNE_START column since we don't need it.
            if non_terminal != COLOGNE_START:
                self.table.update({non_terminal: base_column.copy()})

        # Generate the actions
        for closure_index, closure in enumerate(self.parser.closures):
            # Go over the gotos of the closure
            for goto_symbol, goto_closure in closure.goto.items():
                self.__update_table(goto_symbol, closure_index, TableAction(TableActionType.SHIFT, goto_closure))
            
            # Check for any final productions
            for production in closure.complex_productions:
                # If the production cannot generate more, than it is a final production
                if not production.can_generate_more():
                    if production.result == COLOGNE_START:
                        # We have gotten to the starting production.
                        # Therefore, we can accept
                        self.__update_table(COLOGNE_END, closure_index, TableAction(TableActionType.ACCEPT, 0))
                    else:
                        # We should reduce it.

                        # Find the index of the final production
                        production_index = self.productions.index(production.get_simple_production())

                        # Since right now, the only parser available is LR(0), I am going to hardcode the behavior here.
                        for key in self.table.keys():
                            if key in self.parser.terminals:
                                self.__update_table(key, closure_index, TableAction(TableActionType(TableActionType.REDUCE), production_index))

    def __update_table(self, symbol, closure_index, table_action):
        """
        Updates the table at a given symbol and closure to a new action and infroms the user if there is a conflict.

        :param symbol: The symbol at which to update.
        :type symbol: Symbol

        :param closure_index: The index of the closure at which to update.
        :type closure_index: int

        :param table_action: The new action.
        :type table_action: TableAction
        """

        if not self.table[symbol][closure_index].action == TableActionType.ERROR:
            print(f"Conflict at ({symbol}, {closure_index}).")
            print(f"Previous action: {self.table[symbol][closure_index]}")
            print(f"Current action: {table_action}")

            if input("Would you like to override it (y/n)? ") == "n":
                return
        
        self.table[symbol][closure_index] = table_action













