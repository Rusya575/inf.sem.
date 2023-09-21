a = int(input())
n = list(map(int, input().split()))
s = 0
for i in range(max(s)):
    for j in range(a):
        if min(a) + i == a[j]:
            s += 1
            break
    if s == n//2+1:
        k = i
        break
print(min(a) + k)
