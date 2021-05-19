# def print_employee(**kwargs ):
#     print(kwargs )
# print_employee(id=100,name="jose",salary=50000)

employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

}

#create a function print_employee()=> calling fn print_employee(id=1000) it will name of that employee
def print_employee(**kwargs ):
    id=kwargs ["id"]
    if id in employees :
        print(employees [id]["name"])
    else:
        print("Invalid id")

print_employee(id=1000)




#print(employees )
# def print_employee(**kwargs ):
#     print(kwargs )
#     index=kwargs ['id']
#     d=employees [index ]
#     print(d["name"])
#
#
# print_employee(id=1001)


#
def print_employee(**kwargs ):#kwargs={id:1000,prop:"salary"}
    id=kwargs ["id"]
    prop=kwargs ["prop"]
    if id in employees :
        print(employees [id]["name"])
        print(employees [id][prop ])
    else:
        print("Invalid id")

print_employee(id=1000,prop="salary")