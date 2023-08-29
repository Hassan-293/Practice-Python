def Arr(num):

    temp = []

    for x in num:

        temp.append(x)

    temp.sort()

    return temp

num = [1,0,1,0,0,1]
print(Arr(num))
