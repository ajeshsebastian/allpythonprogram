#local and global variables

# a=10
# def printa():
#     a=1
#     print(a)
# printa()
# print(a)

a=2
def printa():
    global a
    print(a)
    a=a+2
printa()
print(a)