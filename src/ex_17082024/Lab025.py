#Ternery Operator

#if condition then do this
#else do that

#if age>13 then watch reels
#else cant watch

my_age=18
print("I will goa"if my_age>18 else "can't go")

if my_age>18:
    print("Go Goa")

else:
    print("can't goa goa")

    #OR

#print("I will go goa" if int(input("enter your age"))>18 else "can't go goa")

user_age=int(input("enter your age"))

if user_age>18:
    print("Go Goa")

else:
    print("can't goa goa")