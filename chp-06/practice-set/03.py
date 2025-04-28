from simple_chalk import red , green

# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

spam_words = ["buy now", "Make a lot of money", "subscribe this", "click this"]

comment = input("Write a comment: ")


if spam_words[0] in comment:
    print(red("Spam detected!"))
    print("You are banned from the channel")
elif spam_words[1] in comment:
    print(red("Spam detected!"))
    print("You are banned from the channel")
elif spam_words[2] in comment:
    print(red("Spam detected!"))
    print("You are banned from the channel")
elif spam_words[3] in comment:
    print(red("Spam detected!"))
    print("You are banned from the channel")
else:
    print(green("Comment Added ✅"))
    print("Thanks ❤️")