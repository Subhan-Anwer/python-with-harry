import pyjokes
from termcolor import colored

print(colored(pyjokes.get_joke(), 'black', 'on_red', ['bold']))