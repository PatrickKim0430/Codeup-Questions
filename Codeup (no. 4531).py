# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/13
# Problem: Codeup no. 4531 
https://codeup.kr/problem.php?id=4531
# Solution: Using list and append concept to solve this problem


x=[]
for i in range(5):
    x.append(int(input()))

x.sort()
avg=sum(x)//5
print(avg)
print(x[2])
