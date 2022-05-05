# Python startup settings

Make working with command line a little more pleasant with autocomplete,
command history and more.

Run `pip install pyreadline3` (either globally or in each individual
virtual environment).

Using "System Properties" dialog add `PYTHONSTARTUP` variable equal to
`%USERPROFILE%\.pythonstartup.py`.

Create `.pythonstartup.py` file in `%USERPROFILE%` (`C:\Users\myname\`):

```python
try:
    import readline
    import rlcompleter
    readline.parse_and_bind('tab: complete')
except ImportError:
    print('startup: readline not supported')

# For convenience:

import os
import collections
print('startup: imported os, collections')
```

## References

- https://docs.python.org/3/library/rlcompleter.html
- https://docs.python.org/3/library/readline.html
- https://pypi.org/project/pyreadline3/ (tested with Windows 10)

