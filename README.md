# Automation-Countdown

In This Project We Make A Countdown That After Countdown Something Will Happend Like Opening A Browser Maybe ? Or ...

# Usage

Just Simply Import automator like `from automator import *` After That You Have Access To Code. You Can Use This Code Like :

```
from automator import *

countdown = AutomatorCountdown(
    myFunction,
    datetime.time(hour=20, minute=13),
    [],
    {},
    None
)

countdown.run(
    font='univers', # Pyfiglet Fonts
    width=120 # Pyfiglet Line Widths
)
```
