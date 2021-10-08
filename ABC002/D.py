"""
D - 派閥

problem: https://atcoder.jp/contests/abc002/tasks/abc002_4
"""

import itertools

N, M = map(int, input().split())

relations = [[0] * (N+1) for i in range(N+1)]
for i in range(M):
	x, y = map(int, input().split())
	relations[x][y] = 1
	relations[y][x] = 1

result = 0
for bit in range(2 ** N):
	group = []
	for i in range(N):
		if (bit >> i) & 1:
			group.append(i + 1)
	flag = 1
	for j in itertools.combinations(group, 2):
		if relations[j[0]][j[1]] == 0:
			flag = 0
			break
	if flag == 1:
		result = max(result, len(group))

print(result)