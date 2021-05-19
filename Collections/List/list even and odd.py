# Python code to split into even and odd lists
# Funtion to split
# def splitevenodd(A):
l=[2,4,5,6,9,10]
evenlist = []
oddlist = []
for i in l:
     if (i % 2 == 0):
        evenlist.append(i)
     else:
        oddlist.append(i)
print("Even lists:", evenlist)
print("Odd lists:", oddlist)


# Driver Code
# A = list()
# n = int(input("Enter the size of the First List ::"))
# print("Enter the Element of First  List ::")
# for i in range(int(n)):
#     k = int(input(""))
#     A.append(k)
# splitevenodd(A)