# If languages of two friends are same; what will happen to the program in problem 6?

# Problem no # 06

my_dict = {}


friend_1_name = input("Enter your name: ")
friend_1_lang = input("Enter your favorite language: ")

my_dict.update({friend_1_name : friend_1_lang}) # updating name & language of friend 1



friend_2_name = input("Enter your name: ")
friend_2_lang = input("Enter your favorite language: ")

my_dict.update({friend_2_name : friend_2_lang}) # updating name & language of friend 2



friend_3_name = input("Enter your name: ")
friend_3_lang = input("Enter your favorite language: ")

my_dict.update({friend_3_name : friend_3_lang}) # updating name & language of friend 3 



friend_4_name = input("Enter your name: ")
friend_4_lang = input("Enter your favorite language: ")

my_dict.update({friend_4_name : friend_4_lang}) # updating name & language of friend 4

print(my_dict)

#  There will 4 key and value created and two of them wil have the same value, value can be to create a new key value pair, but if the key is same as the existence one the value then only the value is updated