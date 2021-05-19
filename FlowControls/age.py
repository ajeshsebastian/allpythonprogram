
# Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
#
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
#
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#
# And any other input of age should print "ERROR".

# age=int(input("Enter your age "))
# sex=input("Enter your gender M or F")
# mat=input("Enter your marital status")
#
# if(sex=="F"):
#     print("she can only work in urben ")
# elif(sex=="M") and (age>=20 and age<=40):
#     print("he can work in any where")
# elif(sex=="M") and (40<=age<=60):
#     print("he will work in urben areas")
# else:
#     print("error")

age=int(input("Enter age :"))
sex=input("Male(M)/Female(F):")
mat=input("married (Y))/ single(N)")
if(sex=='F'):
    print("you can work")
elif(sex=='M' and (age>=20 and age<=40)):
    print("work any where")
elif(sex=='M' and 40<=age<=60):
    print("you can work urben")
else:
    print("error")