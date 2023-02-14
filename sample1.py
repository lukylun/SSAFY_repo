import random
from pprint import pprint

# n = 5

# arr= [[random.randrange(1, 11) for _ in range(n)] for _ in range(n)]
# print(arr)

# # 절대값의 총합
# abs_sum = 0

# # 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # 행 우선순회
# for i in range(n):
#     for j in range(n):
#         # 현재 위치(x,y)
#         now = arr[i][j]

#         print(f'arr[{i}][{j}] : {arr[i][j]}')

#         # 4방향 탐색하면서 이웃한 원소의 차이의 절대값의 합
#         # 주의할 점: 상하좌우로 움직일 때 유효한 범위(인덱스) 인지 꼭 확인

#         temp_abs = 0 # 현재 위치에서 절대값 차이의 합
#         for d in range(4):
#             nx = i + dx[d]
#             ny = j + dy[d]
#             if 0 <= nx < n and 0 <= ny < n:
#                 # 절대값 계산
#                 temp_abs += abs(arr[i][j] - arr[nx][ny])
#         abs_sum += temp_abs

# print(abs_sum)

# 퀴즈 행5 * 열6 값을 임의로 할당(random)
# 2차원 배열의 모든 원소를 순회하면서 짝수인 원소의 갯수를 세는 프로그램

# n = 5
# m = 6

# arr = [[random.randrange(1,10) for _ in range(m)] for _ in range(n)]
# print(arr)

# # 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# sum_abs = 0 
# for i in range(n):
#     for j in range(m):
#         now = arr[i][j]
        
#         abs_temp = 0 
#         for d in range(4):
#             nx = i + dx[d]
#             ny = j + dy[d]
#             if 0 <= nx < n and 0 <= ny < n:
#                 abs_temp += abs(arr[i][j] - arr[nx][ny])
#         sum_abs += abs_temp

# print(sum_abs)

arr = [3, 1, 2]

n = len(arr)
# 부분집합의 갯수 = 2^n

'''
부분집합에 포함이 되면 1로 표시 / 포함되지 않으면 0으로 체크 => 비트연산
부분집합의 갯수 => 2^n
2^0 2^1 2^2 2^3 2^4 2^5
[3 ,6 ,7, 1, 5, 4]
[1, 0, 0, 1, 1, 0] => 0b011001 => 1 + 8 + 16 + 25 => 25번째 부분집합
[1, 0, 0, 0, 0, 0] => ob000001 => 1번째 부분집합
'''

for i in range(1<<n): # i번째 부분집합에 대해
    print(f'{i}번째 부분집합 : ', end='')
    sub_set = []
    for j in range(n): # i번째 부분집합이 n개의 원소 중에 j번째 원소를 포함하는지 검사
        if i & (1<<j): # i를 이진수로 바꿨을 때 j번째 원소가 1인경우 그 j번째 원소를 포함하는 부분집합
            # print(arr[j], end=', ')
            print(1<<j)
            sub_set.append(arr[j])
    # print(sub_set)

print()