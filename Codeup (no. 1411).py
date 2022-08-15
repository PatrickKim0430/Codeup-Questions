# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/15
# Problem: Codeup no. 1411, A missing card
https://codeup.kr/problem.php?id=1411
# Solution: Using for loop and list to solve this problem

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
