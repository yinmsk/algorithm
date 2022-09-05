"단어 공부"
"https://www.acmicpc.net/problem/1157"


"* 문제"
"알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오."
"단, 대문자와 소문자를 구분하지 않는다."
"첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다."
"출력 예시: 알파벳 대문자로 출력한다"


"lower()는 문자열의 모든 문자를 소문자로 바꾼다. 예를 들어 “Ups AND Downs”.lower()는 ‘ups and downs’로 계산된다."
"upper()는 문자열의 모든 문자를 대문자로 바꾼다. 예를 들어 “Ups AND Downs”.upper()는 ‘UPS AND DOWNS’로 계산된다."
"set()는 집합 함수이다. 중복을 허용하지 않는다. 순서가 없다."
"max()은 인수로 받은 자료형 내에서 최대값을 찾아서 반환하는 함수 입니다."

# 대문자로 바꾼다.
alphabet = input().upper()
# 중복값을 없애고 list에 넣는다
alphabet_list = list(set(alphabet))

cnt = []
for i in alphabet_list:
    cnt.append(alphabet.count(i))

# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우.
if cnt.count(max(cnt)) > 1:
    print("?")
# 해당 index 위치의 알파벳을 출력한다.
else:
    print(alphabet_list[(cnt.index(max(cnt)))])