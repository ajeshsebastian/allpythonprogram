# 5. Python program to check the given sequence is palindrome or not

p=input("Enter the sequence")
c=""
for i in p:
    c=i+c
if (p==c):
    print("The sequence ",p,"is a palindrome")
else:
    print("The sequence ",p,"is not a palindrome")


