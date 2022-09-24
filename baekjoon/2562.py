'''
9개의 숫자가 주어지고
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

입력
3
29
38
12
57
74
40
85
61

출력
85
8
'''


num_list = []

for i in range(9):
    num_list.append(int(input()))

max_num = max(num_list)

print(max_num)
print(num_list.index(max_num) + 1)