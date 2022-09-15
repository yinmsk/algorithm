"곱셈"
"https://www.acmicpc.net/problem/2588"


# 곱하기를 하기 위해서는 str이 아닌 int를 받아야 하니 input() 값을 int()를 사용해 정수로 바꾸어 준다.
a = int(input())
# b를 정수로 바꾸지 않는 이유는 정수는 0번째 1번째가 없기 때문 index는 str만 가능하다.
b = input()

# 예제 출력을 위해 해당 인덱스의 숫자를 a와 곱해준다.
print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
# a 와 b 를 곱한 값을 출력한다.
print(a * int(b))