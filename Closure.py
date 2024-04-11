from ComplexProduction import *

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

    def __neq__(self, other):
        return not self == other

    def create_productions(self, base_production, productions):
        """
        Generates the complex productions for this closure

        :param base_production: The base production in which this closure is based on
        :type base_production: ComplexProduction

        :param productions: All the productions
        :type productions: list

        :returns: Nothing
        :rtype: None
        """
        
        self.__create_productions_recursion(base_production, productions)

    def __create_productions_recursion(self, base_production, productions):
        self.complex_productions.append(base_production)
        
        if base_production.can_generate_more():
            symbol = base_production.get_current_symbol()

            for production in productions:
                if production.result == symbol and production not in self.productions_checked:
                    self.productions_checked.append(production)
                    self.__create_productions_recursion(ComplexProduction(production), productions)

    def generate_next_closures(self, closures, productions):
        """
        Generates the next closures from the current closure.

        :param closures: A list of all the previous closures
        :type closures: list

        :param productions: A list of the previous productions (Passed because we need to
                            pass it to the next closures we are creating).
        :type productions: list

        :returns: Nothing
        :rtype: None
        """
        
        for my_production in self.complex_productions:
            next_closure_index = 0
            
            new_closure = Closure()

            production = my_production.get_prod_next_symbol()

            if production.is_valid():
                new_closure.create_productions(production, productions)
                
                # if check_closure_in_list(new_closure, closures) == False:
                if new_closure not in closures:
                    closures.append(new_closure)
                    next_closure_index = len(closures) - 1

                    closures[-1].generate_next_closures(closures, productions)
                else:
                    next_closure_index = closures.index(new_closure)
                
                # Check if all the productions in this production are final
                cant_add = True

                for complex_production in self.complex_productions:
                    if complex_production.can_generate_more():
                        cant_add = False
                
                if not cant_add:
                    self.goto[production.get_prev_symbol()] = next_closure_index




