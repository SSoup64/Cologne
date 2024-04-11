class Production:
    def __init__(self, result, rule):
        self.result = result
        self.rule = rule

    def __str__(self):
        ret = f"{self.result} ->"

        for symbol in self.rule:
            ret += " " + str(symbol)

        return ret
        
