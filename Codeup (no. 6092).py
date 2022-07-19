# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/20
# Problem: Codeup no,6092, An odd attendance call
https://codeup.kr/problem.php?id=6092
# Solution: Using for loop and list to solve this problem

n=int(input())
a= input().split()
l=[]

for i in range(n):
    a[i]=int(a[i])


for i in range(24):
    l.append(0)

for i in range(n):
    l[a[i]] = l[a[i]] + 1

for i in range(1,24):
    print(l[i], end = " ")
