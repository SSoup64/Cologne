
# A parent class for terminals and non-terminals
class Symbol:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
