#1
#1 2
#1 2 3

for i in range(1,4):            #1       2        3
    for j in range(1,i+1):      #1,2    1,3      1,4
      print(j,end=" ")          #1       1 2      1,2,3
    print("")