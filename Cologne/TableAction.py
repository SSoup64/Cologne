from enum import Enum

class TableActionType(Enum):
    SHIFT = 0,
    REDUCE = 1,
    ERROR = 2,
    ACCEPT = 3,

class TableAction:
    def __init__(self, action, goto):
        """
        Creates a new table action.

        :param action: Which action is taken.
        :type action: TableActionType

        :param goto: To which state to go after the action is executed.
        :type goto: int

        :returns: THe new object
        :rtype: TableAction
        """

        self.action = action
        self.goto = goto

    def __str__(self):
        """
        The string representation of a table action

        :returns: the string representation of the table action
        :rtype: str
        """

        ret = ""

        if self.action == TableActionType.SHIFT:
            ret = f"Shift-{self.goto}"
        elif self.action == TableActionType.REDUCE:
            ret = f"Reduce-{self.goto}"
        elif self.action == TableActionType.ERROR:
            ret = ""
        elif self.action == TableActionType.ACCEPT:
            ret = "Accept"
        
        return ret

