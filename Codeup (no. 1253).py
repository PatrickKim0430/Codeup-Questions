# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/16
# Problem: Codeup no,1253, Outputs from a to b
https://codeup.kr/problem.php?id=1253
# Solution: Using if and else statement to solve this problem

a,b=input().split()
a=int(a) # 3 
b=int(b) # 8

if a > b:  # 5, 3 
    for i in range(b,a+1):
        print(i, end =" " ) 
else:  # 3, 5 
    for i in range(a, b+ 1):
        print(i, end = " ")
