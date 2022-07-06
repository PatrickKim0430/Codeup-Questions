n = int(input())
a = []
b = []

for i in range(1, n+1):
    a.append(i)

for i in range(0, n-1):
    num = int(input())
    b.append(num)

for card in b:
    a.remove(card)

print(a[0])
