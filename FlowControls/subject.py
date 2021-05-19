# 4 subject mark
# total
# 180-200 A+
# 160 -179 A
# 140-159 B+
# 120-139B
# 100-110 C+
# 80-99 C
# 68-79 D+
# Fail

num1 = int(input("mark of subject one"))
num2 = int(input("mark of subject two"))
num3 = int(input("mark of subject three"))
num4 = int(input("mark of subject four"))

total = num1 + num2 + num3 + num4
print(total)
if (total >= 180):
    print("A+")
# elif(total=>160) and (total<=179):
elif 160 <= total <= 179:
    print("A")
# elif(total>=140) and (total<=159):
elif 140 <= total <= 159:
    print("B+")
# elif(total>=120) and (total<=139):
elif (120 <= total <= 139):
    print("B")
# elif(total>=100) and (total<=119):
elif (100 <= total <= 119):
    print("C+")
# elif(total>=80) and (total<=99):
elif (80 <= total <= 99):
    print("C")
# elif(total>=68) and (total<=79):
elif (68 <= total <= 79):
    print("D+")
else:
    print("Fail")

# print(total)
