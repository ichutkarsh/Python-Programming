
# Array program for sum of an array items
num = list(map(int,input("enter your input for array--> ").split()))

max = 1
for i in num:
    if max<i:
        max = i
print(max)


