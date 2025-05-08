# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
from simple_chalk import red, green

with open('poems.txt') as poem:
    poem_text = poem.read()
    
if 'twinkle' in poem_text.lower():
    print(green("twinkle is in the poem"))
else:
    print(red("twinkle is in not the poem"))
