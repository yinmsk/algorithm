"더하기 싸이클"
"https://www.acmicpc.net/problem/1110"

'''
문제
0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.
26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.

예시)
초기 입력값 26
2+6 = 8이다. 새로운 수는 68이다.
6+8 = 14이다. 새로운 수는 84이다.
8+4 = 12이다. 새로운 수는 42이다.
4+2 = 6이다. 새로운 수는 26이다.
4번 돌았으니 출력값은 4가 나와야 한다.
'''


N = int(input()) # 초기 입력값
num = N 
count = 0 # 사이클 수

while True: # True 일 경우 계속 반복
    count += 1 # 반복이 돌 때마다 +1을 한다.
    a = num//10 # 입력값을 10으로 나눈 다음 그 몫을 가져온다. 예를들어 68이 입력값이라면
                # a라는 변수 안에는 1이 들어가야 한다. 68/10의 몫은 6이므로 원하는 값을 가져올 수 있다.
    b = num%10 # 입력값을 10으로 나눈 다음 나머지를 가져온다. 입력값이 68 이니까
               # b라는 변수 안에는 8이 들어가야 한다. 68/10의 나머지는 8이므로 원하는 값을 가져올 수 있다.
    c = (a+b)%10 # (6+8=14)%10 의 값은 4이다.
    num = (b*10)+c # (8*10=80)+4 는 84
    if N==num: # 초기 입력값과 더한 값이 값다면 while문을 종료하고 몇번 반복했는지 print 한다.
        break
print(count)