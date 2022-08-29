# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/29
# Problem: Codeup no. 2721, Cyclic String
https://codeup.kr/problem.php?id=2721
# Solution: Using if statement and iinput() to solve this problem

S1 = input()
S2 = input()
S3 = input()

if S1[-1] == S2[0]:
    if S2[-1] == S3[0]:
        if S3[-1] == S1[0]:
            print("good")
        else:
            print("bad")
    else:
        print("bad")
else:
    print("bad")

