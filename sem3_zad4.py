a = input().split()
for i in range ( 0, len(a) - 1, 2):
    s[i], a[i+1] = a[i+1], a[i]
print(a)
