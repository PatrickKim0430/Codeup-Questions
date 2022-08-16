# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/16
# Problem: Codeup no. 1548, Return grade as a function
https://codeup.kr/problem.php?id=1548
# Solution: Using if statement and function to solve this problem

def grade(n):
    if 90<=n<=100:
        print("A")
    elif 80<= n <90:
        print("B")
    elif 70 <= n < 80:
        print("C")
    elif 60<= n < 70:
        print("D")
    else:
        print("F")
n=int(input())
grade(n)            
