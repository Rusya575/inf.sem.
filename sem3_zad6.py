a = list(map(int, input().split()))
for i in range(len(a)):
    if n.count(a[i]) == 1:
        print(a[i])
