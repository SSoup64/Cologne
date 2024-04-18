class Production:
    def __init__(self, result, rule):
        self.result = result
        self.rule = rule

    def __str__(self):
        ret = f"{self.result} ->"

        for symbol in self.rule:
            ret += " " + str(symbol)

        return ret

    def __eq__(self, other):
        if not isinstance(other, Production):
            return False

        return self.result == other.result and self.rule == other.rule
    
    def __ne__(self, other):
        return not (self == other)


