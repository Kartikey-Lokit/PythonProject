#condition and Loop

#Write program to take user age and let user know if he go to club.
#21

# Logic Building
#User Input-date type--> int
#o/p -> string --> user if he go or not

# 2. Rough Logic
#age>21 --> Print can go
#<21--> Print can;t go
#f-->f is string formating
# write logic

age=input("Enter yur age\n")
age=int(age)

if age>21:

    print("can go club --> {age}")

else:

    print(f"Can't go to club --> {age}")
