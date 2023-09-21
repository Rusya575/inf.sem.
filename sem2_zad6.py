f = open('input.txt')
a = []
for line in f:
    a.append(line)
c = a[0].split()
e = a[1]
e = e[0]
for i in range(len(c)):
    c[i] = str(int(c[i], int(a[2])))
if e == '+':
    z = 0
    for i in range(len(c)):
        z += int(c[i])
if e == '-':
    z = int(c[0])
    for i in range(1, len(c)):
        z -= int(c[i])
if e == '*':
    z = 1
    for i in range(len(c)):
        z *= c[i]
r = ''
while z != 0:
    r = r + str(z % int(a[2]))
    z = z // int(a[2])
f1 = open('output.txt','w')
f1.write(str(r[::-1]))
f1.close()
