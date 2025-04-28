from simple_chalk import green , red

# Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Write a post: ")
word = "Harry"

if word in post:
    print(green('Yes'), ', this post is talking about "Harry"')
else :
    print(red('No'), ', this post is not talking about "Harry"')