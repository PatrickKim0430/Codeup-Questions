# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/29
# Problem: Codeup no. 1402  
https://codeup.kr/problem.php?id=1402
# Solution: Using list and for loop to solve this problem

n=int(input())
a=list(map(int,input().split()))
a.reverse() 

for i in a: 
    print(i,end=" ")
