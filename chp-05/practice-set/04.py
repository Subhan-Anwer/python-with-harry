# What will be the length of following set s: 
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 

# My answer is the length of this set should be 3 as at first it was empty so 0 
# then we added 20 (integer) so now 1 
# then we added 20.0 (float) so now 2
# the we added '20' (string) so now 3

# Lets check that 
print(len(s))
print(s)

# All right i'm wrong the python count 20.0 and 20 as same i thought the python will count 20.0 as decimal and floating data type so it will be different but its same so python will assign type int to both and hence wont count twice, only register once so the lenght of s will be 2

# i'm not gonna delete my guess or correct i learned something from my mistake!