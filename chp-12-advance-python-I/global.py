a = 60

def fun(num: int) -> int:
    global a
    a = num
    print("function runnning...")
    
    
print(f"a before: {a}")
fun(101)
print(f"a after: {a}")