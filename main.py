"""
Write a program that asks a user for a three digit integer. Add the digits together and print the sum. 
"""
nums = int(input("Give me a 3 digit number "))
one = nums % 10
deci = nums % 100 // 10
centi = (nums - deci) //100
print (one+deci+centi)
