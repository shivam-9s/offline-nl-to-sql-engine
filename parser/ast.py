class QueryNode:
    def __init__(self, action, table=None, columns=None, conditions=None):
        self.action = action
        self.table = table
        self.columns = columns or []
        self.conditions = conditions or []  # List of condition dicts
