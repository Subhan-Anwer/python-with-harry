# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ****** by updating the same file.

f = open("donkey_text.txt")
data = f.read()
# print(data)
f.close

for donkey in data.lower():
    with open("donkey_text.txt", "w") as f:
        f.write(data.replace("donkey", "******"))