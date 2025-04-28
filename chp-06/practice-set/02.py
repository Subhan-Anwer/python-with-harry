from simple_chalk import red, green

# getting english marks and checking for 33% if passed prints English Passed ✅ otherwise prints English Passed ✅

english = int(input("Enter marks in english: "))
english_passed = False
if (english >= 33):
    print(green("English Passed ✅"))
    english_passed = True
else:
    print(red("English Failed ❌"))
    

# getting mark marks and checking for 33% if passed prints Math Passed ✅ otherwise prints Math Passed ✅
math = int(input("Enter marks in math: "))
math_passed = False
if (math >= 33):
    print(green("Math Passed ✅"))
    math_passed = True
else:
    print(red("Math Failed ❌"))
    

# getting urdu marks and checking for 33% if passed prints Urdu Passed ✅ otherwise prints Urdu Passed ✅
urdu = int(input("Enter marks in urdu: "))
urdu_passed = False
if (urdu >= 33):
    print(green("Urdu Passed ✅"))
    urdu_passed = True
else:
    print(red("Urdu Failed ❌"))
    
    
sum_marks = english + math + urdu


if (sum_marks / 300 * 100 >= 40 and english_passed and math_passed and urdu_passed):
    print(green("Congratulations! you have passed all papers"))
    print(f"Your Percentage is {sum_marks / 300 * 100}%" )
else : 
    print("")
    print(red("You are Failed"))
    