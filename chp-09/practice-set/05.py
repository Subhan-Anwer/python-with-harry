# Repeat program 4 for a list of such words to be censored.

f = open("spam.txt")
data = f.read()
f.close

censored_word = ["loser", "pyramid", "scheme", "credit card", "vViagra", "shit", "porn", "idiot", "bitch", "dumb"]

for word in censored_word:
    data = data.replace(word, "****")
    
    
with open("spam.txt", "w") as f:
    f.write(data)
        
        
        