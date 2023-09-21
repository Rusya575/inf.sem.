n, b, c = str(input()), int(input()), int(input())
a = int(n, b)
g = ''
while a != 0:
    g = g + str(a % c)
    a = a // c
print(g[::-1])
    
