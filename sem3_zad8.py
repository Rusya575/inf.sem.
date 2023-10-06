a = int(input())
n = list(map(int, input().split()))
s = 0
for i in range(max(n)):
    for j in range(a):
        if min(n) + i == n[j]:
            s += 1
            break
    if s == a//2+1:
        k = i
        break
print(min(n) + k)
