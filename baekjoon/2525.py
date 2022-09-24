'''
오븐시계
https://www.acmicpc.net/problem/2525
'''
'''
# 내가 풀이한 방식
H, M = map(int, input().split())
required_time = int(input())

M += required_time

while M > 59:
    if M > 59:
        M -= 60
        H += 1

    if H > 23:
        H -= 24

print(H, M)
'''

H, M = map(int, input().split())
required_time = int(input())

H += required_time // 60
M += required_time % 60

if M > 59:
    M -= 60
    H += 1

if H > 23:
    H -= 24

print(H, M)