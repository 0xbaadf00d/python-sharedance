python-sharedance
=================

Sharedance class for Python.

## sharedance.py
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

## django-sharedance-session.py
```python
# Put this in your settings.py
SESSION_ENGINE  = 'sharedance.django-sharedance-session' #adapt this line to your project
SHAREDANCE_HOST = '127.0.0.1'
SHAREDANCE_PORT = 1042
```
