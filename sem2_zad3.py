a = input().split()
n = len(a)
s = 1
for i in range(n):
    i = a[i]
    s *= i
print(s**(n**(-1)))
    
