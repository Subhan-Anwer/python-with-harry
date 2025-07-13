# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old. 

for t in range (2 ,21):
    with open(f"13_year_old/{t}_table.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{t} x {i} = {t*i}")
            if i < 10:
                f.write("\n")
            else:
                f.write(" ")