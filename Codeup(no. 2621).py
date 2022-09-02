# Programmer:  Patrick Junhee Kim 
# Date: 2022/9/2
# Problem: Codeup no. 2621. The Sum of divisor
https://codeup.kr/problem.php?id=2621
# Solution: Using function and for loop to solve this problem

def solution(n):
    answer = 0 
    for i in range(1, n+1) :
        if n % i == 0 :
            answer += i
    return answer


n = int(input())

print(solution(n))
