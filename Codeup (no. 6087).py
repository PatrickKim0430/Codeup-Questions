# Programmer:  Patrick Junhee Kim 
# Date: 2022/9/22
# Problem: Codeup no. 6087, 3 multiple
https://codeup.kr/problem.php?id=6087
# Solution: Using for loop and int(input()) to solve this problem

n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    else:
        print(i, end=' ')
