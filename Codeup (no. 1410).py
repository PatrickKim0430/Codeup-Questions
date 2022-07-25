# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/25
# Problem: Codeup no. 1410
https://codeup.kr/problem.php?id=1410
# Solution: Using for loop and if statement to solve this problem

n=input() 
open = 0
close = 0 

for i in range(0,len(n)):
    if n[i] == "(":
        open = open +1
    elif n[i] == ")":
        close = close +1 

print(open, close)
