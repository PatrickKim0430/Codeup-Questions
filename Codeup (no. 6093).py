# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/31
# Problem: Codeup no. 6093
https://codeup.kr/problem.php?id=6093
# Solution: Using for loop and int(input()) to solve this problem

n=int(input())
a = input().split()

for i in range(n):
    a[i]=int(a[i])

for i in range(n-1, -1, -1):
    print(a[i], end= " ") 
