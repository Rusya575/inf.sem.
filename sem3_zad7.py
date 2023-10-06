a = list(map(int, input().split()))
m = 0
for i in range(len(a)):
    if a.count(a[i]) >= m:
        m = a.count(a[i])
        z = a[i]
print(z)
