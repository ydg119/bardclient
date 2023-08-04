# bardclient
A simple reverse engineering of google's bard implements by python3

## Installation
```bash
$ pip3 install --upgrade bardclient
```

## Authentication
Go to https://bard.google.com/

- F12 for console
- Copy the cookie value
> Path: Application -> Cookies -> `__Secure-1PSID`, Copy the value of the cookie.

## Usage
### Implementation
```python
from os import environ

from bardclient import BardClient

bard_token = environ.get('BARD_TOKNE')
bot = BardClient(bard_token)
res_message = bot.ask('Hi, how are you?')

print(res_message["content"])
```