num = input().split()
for i in range(1, int(num[0])):
    b = num.count(str(i))
    if b == 0:
        break
    elif i == int(num[len(num)-1]):
        i += 1
        break
print(i)
               
    
