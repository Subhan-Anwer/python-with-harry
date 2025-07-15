# Q1. Create two virtual environments, 
#     install few packages in the first one.
#     How do you create a similar environment in the second one?


# created two virtual environments env1 and env2 using virtualenv env1 and virtualenv env2

# installed few packages in env1 by first activating the environment and then installing the packages
# you can see installed packages in an environment by using pip freeze and also record that packages in a file using pip freeze > requirements.txt

# duplicating the requirement.txt file in env2 to install same 
# deactivating env1, and activating env2

# pip install -r requirements.txt to install same packages