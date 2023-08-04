from os import environ

from bardclient import BardClient

bard_token = environ.get('BARD_TOKNE')
bot = BardClient(bard_token)
res_message = bot.ask('Hi, how are you?')
print(res_message["content"])
