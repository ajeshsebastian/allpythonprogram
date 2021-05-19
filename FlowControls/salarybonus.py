#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.

salary=int(input("Enter your salary"))
service=int(input("Enter your year of service"))
if(service>=5):
    bonus=(salary/100)*5
    print("eligible bonus is",bonus)
else:
    print("not eligible for bonus")
   #bonus=(salary/100)*5
    #print(bonus)                                            
