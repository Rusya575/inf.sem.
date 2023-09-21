f = open('input.txt')
a = []
for line in f:
    a.append(line)
c = a[0].split()
e = a[1]
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
f1 = open('output.txt','w')
f1.write(str(z))
f1.close()
