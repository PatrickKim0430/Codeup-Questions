# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/10
# Problem: Codeup no,1260, the sum of the multiples of three  
https://codeup.kr/problem.php?id=1260
# Solution: Using for loop concept to solve this problem

a,b=input().split()
a=int(a)
b=int(b)
count=0

for i in range(a, b+1):
    if i % 3 ==0:
        count=count+i

print(count) 
