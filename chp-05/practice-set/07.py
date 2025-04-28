my_dict = {}


friend_1_name = input("Enter your name: ")
friend_1_lang = input("Enter your favorite language: ")

my_dict.update({friend_1_name : friend_1_lang})



friend_2_name = input("Enter your name: ")
friend_2_lang = input("Enter your favorite language: ")

my_dict.update({friend_2_name : friend_2_lang})



friend_3_name = input("Enter your name: ")
friend_3_lang = input("Enter your favorite language: ")

my_dict.update({friend_3_name : friend_3_lang})



friend_4_name = input("Enter your name: ")
friend_4_lang = input("Enter your favorite language: ")

my_dict.update({friend_4_name : friend_4_lang})

print(my_dict)


# above is program / problem 6

# If the names of 2 friends are same; what will happen to the program in problem 6?

# The the names of 2 friends are same the python will update the value of key value pair which has same key and the value update according to the last value passed to the same key

# for example if two friends name are same lets say Shubh and we pass it like that in input
# friend_1_name = "Shubh" , friend_1_lang = "Hindi"
# # friend_2_name = "Shubh" , friend_2_lang = "Punjabi" 

# at first the python will create a key valur pair for Shubh (key) and Hindi (value)
# then when we pass the same key Shubh again it will update the value we are passing to Shubh key which is already existing, hence update Hindi to Punjabi, not creating another key value pair
