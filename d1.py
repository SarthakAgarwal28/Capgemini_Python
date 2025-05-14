'''
print("India will win the war!")
print(100, 200, sep ="$", end = "@")
print(500, 400, sep ="#", end = "@\n")

print(1, 1000, sep ="-", end = "&")
print(10, 20, sep ="-", end = "#")
print(30, 40, sep ="@", end = "#")
'''
'''
a, b, c = 10, 20, 30
print(f"a = {a} b = {b} c = {c}")
'''
# s = float("10.5")
# print(type(str(s)))
# a = 100.88
# b = "Hello"
# print(type(bool(a)))
# print(type(bool(b)))

# print(str(input()))
# print(bool(0))
# print(10*20)
# print(10*20.2)
# print(5*"2")
# print(3*"2.0")
# print("20"*"4")
# a =4
# print("ab"*a)

# print("ab">"cd")
# print("ab"<"cd")
# print(ord('a'))
# print(ord('A')) 
# print(chr(97))
# print(chr(65))
# print("a" == "A")
# print("a" != "A")
# print(chr(97,65))
# print(1012%10)
# print(1012//10)
# print('A'<=input()<='Z') #For Uppercase
# print('a'<=input()<='z') #For Lowercase
# print('0'<=input()<='9') #For Digits
# print('A'<=input()<='Z' or 'a'<=input<='z') #For Alphabets
# Three examples on and or not
# print('A'<=input()<='Z' and 'a'<=input()<='z') #For Uppercase and Lowercase
# print('A'<=input()<='Z' or 'a'<=input()<='z') #For Uppercase or Lowercase
# print(not 0) #For Uppercase and not Lowercase
# print(bin(145))
# print(bin(123))
# print(bin(145&123))
# x = 4
# x%=6
# print(x)
# x**=2
# print(x)
# x//=2
# print(x)
# x&=2
# print(x)
# x|=2
# print(x)
# x^=2
# print(x)
# x= 9
# #x~=2 not an operator
# print(x)
# x>>= 2
# print(x)
# x<<= 2
# print(x)
# x-=3
# print(x)

# Membership operator
# print("" in "sarthak")
# print("" not in "sarthak")
# print('' not in 'sarthak ')
# print('' in 'sarthak ')
#slicing is used in strings and lists
# print("python"[2:6]) # thon
# print("python"[1:6:2])  # yhn
# print("python"[-5:6:2]) # yhn
#print("python"[-1:-7:-1]) # nohtyp
#print("python"[::-1]) # nohtyp
# print("python"[2:]) # thon
# print("python"[:6]) # python
# print("python"[:]) # python

# Dot Operators
#print("RCBCskmit".isalpha()) # True
# print("RCBCSKMI".isupper()) # True
# print("rcbskmit".islower()) # True
# print("12345".isnumeric()) # True
# print("12345".isdecimal()) # True
# print("12345".isdigit()) # True
# print("var".isidentifier()) # True
# print("12345".isprintable()) # True
# print("12345abcde".isalnum()) # True
# control statements
# if else
# elif
# match case
# TO CHECK IF NUMBER IS 2 DIGIT
# num = int(input("Enter a number: "))
# num = 12
# if num>=10 and num<=99:
#     print("True")
# else:
#     print("RCB")
# # TO CHECK IF NUMBER IS both 2 DIGIT AND 3 digit
# num = int(input("Enter a number: "))
# if num>=10 and num<=99:
#     print("Double Digit")
# elif num>=100 and num<=999:
#     print("Triple Digit")
# else:
#     print("Other Digit")
# # TO CHECK IF NUMBER IS DIVISIBLE BY 5 AND 7 USING NESTED IF ELSE
num = int(input("Enter a number: "))
if num%5==0:
    if num%7==0:
        print("Divisible by 5 and 7")
    else:
        print("Divisible by 5")
else:
    if num%7==0:
        print("Divisible by 7")
    else:
        print("Not Divisible by 5 and 7")