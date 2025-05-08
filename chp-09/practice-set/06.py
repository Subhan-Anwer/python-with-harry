# Write a program to mine a log file and find out whether it contains ‘python’.

with open("log.txt") as f:
    data = f.read()
    
detector = data.count("python")
# print(detector)

if detector > 0 :
    print(f"✅ The word Python is found {detector} times in log.txt")
else:
    print("❌ The word Python does not found in the file")