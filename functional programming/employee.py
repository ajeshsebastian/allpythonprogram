employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
     {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]

# emp_name=list(map(lambda emp:emp["name"],employees ))
# print(emp_name )
# emp_sal=list(map(lambda emp:emp ["eid"],employees )   )
# print(emp_sal )

# #filter
# def get_dev(emp):
#     return emp["designation"]=="developer"

#deve=list(filter(lambda emp:)
# dev=list(filter(lambda emp:emp["designation"]=="developer",employees  ) )
# deve=list(map(lambda emp:emp["name"],dev ))
# print(deve )

#list compre

ename=[emp["name"] for emp in employees ]
print(ename )

emname=[emp  for emp in employees if emp["designation"]=="developer"]
print(emname )

high=max([emp["salary"] for emp in employees ])
print(high )


# reduce this to single line
developer=list(map(lambda emp:emp["name"],list(filter(lambda emp:emp["designation"]=="developer",employees ))))
print(developer )
#print develope name

# lst=[7,8,9,4,3,2]
#
# num=list (filter(lambda number:number>5,lst))
# print(num )



