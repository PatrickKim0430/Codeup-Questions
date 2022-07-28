# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/28
# Problem: Codeup no,1355 
https://codeup.kr/problem.php?id=1355
# Solution: Using for i loop and for j loop to solve this problem

n=int(input()) # 3

for i in range(1, n+1): # 1, 2, 3 
    for j in range(1, i): # 
        print(' ', end = '')
    for j in range(i, n+1):
        print('*', end = '')
    print()
