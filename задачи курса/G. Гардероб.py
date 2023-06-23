n = int(input())
array = input().split()
pink = []
yellow = []
crimson = []
for x in array:
    if x == '0':
        pink.append(x)
    elif x == '1':
        yellow.append(x)
    else:
        crimson.append(x)
print(*(pink + yellow + crimson))
