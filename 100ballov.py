''''''
# hard
a = [int(i) for i in open("17hard.txt")]
k = 0
mn = 10**10
para = []
fib = [0, 1]
while fib[-1] <= 150_000:
    teckuchee = fib[-1] + fib[-2]
    fib.append(teckuchee)
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        para.clear()
        para.append(a[i])
        para.append(a[j])
        para.sort()
        if a[i] != a[j]:
            if para[0] in fib and para[1] in fib:
                tr1 = fib.index(para[0])
                tr2 = fib.index(para[1])
                if (tr1 + 1) == tr2:
                    k += 1
                    mn = min(mn, a[i] + a[j])
print(k, mn)
'''
"""
#medium
a = [int(i) for i in open("17medium.txt")]
k = s = 0
for i in range(len(a)):
    for x in range(i + 1, len(a)):
        for y in range(x + 1, len(a)):
            for z in range(y + 1, len(a)):
                if a[i] != 0 and a[x] != 0 and a[y] != 0 and a[z] != 0:
                    storony = [a[i], a[x], a[y], a[z]]
                    storony.sort()
                    if storony[0] == storony[1] and storony[2] == storony[3]:
                        k += 1
                        s = max(s, storony[0] * storony[3])
print(k, s)

#easy
a = [int(i) for i in open("17easy.txt")]
k = 0
mx = 0
alf = [111, 222, 333, 444, 555, 666, 777, 888, 999]
for i in range(len(a) - 1):
    if a[i] in alf and a[i + 1] in alf:
        k += 1
        mx = max(mx, a[i] + a[i + 1])
print(k, mx)
"""
