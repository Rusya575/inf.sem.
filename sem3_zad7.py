a = list(map(int, input().split()))
m = 0
for i in range(len(a)):
    if n.count(a[i]) >= m:
        m = a.count(n[i])
        z = a[i]
print(z)
