python-sharedance
=================

Sharedance library for Python.

```python
from sharedance import Sharedance

hDance = Sharedance()
hDance.Set("user", {"id":42, "login":"toto", "email":"mail@localhost"})
hDance.Set("str", "my great string")
print hDance.Fetch("user")
hDance.Delete("user")
hDance.Delete("str")
hDance = None
```