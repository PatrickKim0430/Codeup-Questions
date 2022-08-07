# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/7
# Problem: Codeup no,1902, Recursive function
https://codeup.kr/problem.php?id=1902
# Solution: Using function and if statement to solve this problem

n=int(input()) #4
def number(n): #number(4)
    if n == 1:  
        print(n)
    else:
        print(n)
        number(n-1)

number(n) 
