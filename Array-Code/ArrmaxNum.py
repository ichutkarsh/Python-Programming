
# Array for finding max number in a array/list
num = list(map(int,input("enter your input for array--> ").split()))

max = 1
for i in num:
    if max<i:
        max = i
print(max)


