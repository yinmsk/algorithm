'''
X보다 작은 수
https://www.acmicpc.net/problem/10871

예제 입력값
10 5
1 10 4 9 2 3 8 5 7 6

출력
1 4 2 3
'''


N, X = map(int, input().split())
A = list(map(int, input().split()))

low_num=[]
for num in A:
    if num < X:
        low_num.append(str(num))

print(' '.join(low_num))
