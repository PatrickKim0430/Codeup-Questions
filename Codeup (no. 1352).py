# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/7
# Problem: Codeup no,1352, Output Rectangle 1
https://codeup.kr/problem.php?id=1352
# Solution: Using input and for loop to solve this problem

n=int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print("*", end="")
    print(" ")
