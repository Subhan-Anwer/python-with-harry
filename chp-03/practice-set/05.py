# Write a program to format the following letter using escape sequence characters. 

letter = "Dear Harry, this python course is nice. Thanks!"

# Solution # 01
# format_ltr = letter.replace(", ", "\n")
# format_ltr = format_ltr.replace(". ", "\n")

# Solution # 02
format_ltr = letter.replace(", ", "\n").replace(". ", "\n")

print(format_ltr)