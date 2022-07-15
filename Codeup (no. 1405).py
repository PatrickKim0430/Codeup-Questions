# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/15
# Problem: Codeup no. 1405  
https://codeup.kr/problem.php?id=1405
# Solution: Using list and append concept to solve this problem

n=int(input())
a=list(map(int,input().split())) 
# input().split()
for i in range(n):
    for j in a: 
        print(j, end=" ")
    print() 
    a.append(a[0])
    a.pop(0)
    
