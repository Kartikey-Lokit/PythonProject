#match statement=Match the output and execute.
from unittest import case

# Write a programe to ask the user which browser he want to run automation

browser_name=input("enter the name of browser\n")
match browser_name:
case "firefox":
print("execute the firefox code")
case "chrome":
print("execute the chrome code")
case "edge":
print("execute the edge code")
case "safari":
print("execute the safari code")
case _:
print("Browsre not found")

