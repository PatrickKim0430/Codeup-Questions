# Programmer:  Patrick Junhee Kim 
# Date: 2022/11/20
# Problem: Codeup no,1412, Number of Alphabet
https://codeup.kr/problem.php?id=1412
# Solution: Using for loop and list to solve this problem

str = input()
li = [0 for _ in range(26)]
for i in str:
    if i>='a' and i<='z':
        li[ord(i)-97]+=1
    
for i in range(26):
    print("%c:%d" %(chr(i+97),li[i]))
