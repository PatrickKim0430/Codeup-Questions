# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/28
# Problem: Codeup no. 1901, Output from 1 to n (recursive function)
https://codeup.kr/problem.php?id=1901
# Solution: Using function and int(input()) to solve this problem

n=int(input())
def number(n):
    if n != 1: 
        number(n-1)
    print(n)


number(n) 
