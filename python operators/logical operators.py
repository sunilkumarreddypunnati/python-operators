'''Logical (and, or, not)
Write a program to check if a number is between 10 and 50.
Use or for multiple conditions (ex: divisible by 3 or 5)
Use not to invert a condition'''
a=int(input("enter a number:"))
if a>=10 and a<=50:
    print("number is in between 10 and 50:",a)
else:
    print("number is not in between 10 and 50")
if a%3==0 or a%5==0:
    print("give number is divisible by 3 or 5:",a)
else:
    print("give number is not divisible by 3 or 5")
if not a%2==0:
    print("print give number is odd")
else:
    print("given number is even")
