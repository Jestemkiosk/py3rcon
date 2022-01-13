# py3rcon
RCON API for Python3
[![Downloads](https://pepy.tech/badge/py3rcon)](https://pepy.tech/project/py3rcon)

Built and tested for Quake3, but will work with most RCON systems.

## Installation:

`$ pip install py3rcon`

## Examples:

Send RCON commands without waiting for a response:
```python
from py3rcon import RCON

rcon = RCON("127.0.0.1", "secret_password") 
rcon.send_command("say Hello, world!", response=False)
```

Send RCON commands and get their response:
```python
from py3rcon import RCON

rcon = RCON("127.0.0.1", "secret_password", port=27960) #port is optional
status = rcon.send_command("status") 
print(status)
```
