#age calculate

current_year=int(input("Enter current year"))
current_month=int(input("Enter current month"))
current_date=int(input("Enter the current date"))

birth_year=int(input("Enter birth year"))
birth_month=int(input("Enter birth month"))
birth_date=int(input("Enter birth date"))

# age_year=current_year-birth_year
# age_month=current_month -birth_month
# age_date=current_date-birth_date

# print(age_year,"Year",age_month,"Month",age_date ,"days older")

# if(age_year==0):
#     print(age_month)
#          if(age_month==0):
#               print(age_date)
#               else(age_date==0):
#                    print("New Born")
# else:
#     print(age_year ,"old")
# if(age_year ==0) and (age_month !=0):
#     print(age_month, "Month",age_date ,"Days Old" )
# elif(age_year ==1):
#     print(age_month)
#
# elif(age_month ==0)and (age_date!=0):
#     print(age_date,"Days Old" )
# #elif(age_month ==0)(age_date ==0):
#     #print("New Born")
# else:
#     print(age_year ,"Year Old")
# if(age_year==0):
#     if(age_month ==0):
#         print(age_date )
#     else:
#         print("new")
# elif(age_month!=0):
#     print(age_month)
# else:
#     print(age_year)

month=[31,28,31,30,31,30,31,31,30,31,30,31]
if(birth_date > current_date ):
    current_month = current_month -1
    current_date =current_date + month[birth_month -1]
if(birth_month >current_month ):
    current_year =current_year -1
    current_month =current_month +12
age_year=current_year-birth_year         
age_month=current_month -birth_month
age_date=current_date-birth_date
if(age_year ==0) and (age_month !=0):
    print(age_month,"month",age_date ,"days old")
elif(age_month ==0):
    print(age_date ,"days old")
elif(age_year !=0):
    #print(age_year )
#else:
    print(age_year ,"year",age_month ,"months",age_date,"days old")
