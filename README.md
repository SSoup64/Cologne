# COLOGNE
## What Cologne is:
Cologne is a LR(0) parser created in Python.

## How to use cologne:
1. import Cologne.
```Python
import Cologne
```

2. create a parser.
```Python
parser = Cologne.parser
```

3. create your terminals.
```python
# Terminals.
NUMBER = parser.add_terminal(Cologne.Terminal("NUMBER"))
PLUS = parser.add_terminal(Cologne.Terminal("PLUS"))
MINUS = parser.add_terminal(Cologne.Terminal("MINUS"))
TIMES = parser.add_terminal(Cologne.Terminal("TIMES"))
DIVIDE = parser.add_terminal(Cologne.Terminal("DIVIDE"))
```

4. create your non terminals.
```Python
expr = parser.add_non_terminal(Cologne.NonTerminal("expr"))
```

5. create your productions.
```Python
parser.add_productions(
	Cologne.Production( expr, (expr, PLUS, expr) ),
	Cologne.Production( expr, (expr, MINUS, expr) ),
	Cologne.Production( expr, (expr, TIMES, expr) ),
	Cologne.Production( expr, (expr, DIVIDE, expr) ),
	Cologne.Production( expr, (NUMBER, ) )
)
```

6. Generate the closures and the parse table.
```Python
parser.generate_closures()
parse_table = Cologne.ParseTable(parser)
```
