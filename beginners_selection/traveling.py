"""
ABC086C - Traveling
problem: https://atcoder.jp/contests/abs/tasks/arc089_a
"""

N = int(input())
travel = []
for i in range(N):
	t, x, y = map(int, input().split())
	travel.append((t, x, y))

pos = (0, 0, 0)
for i in range(len(travel)):
	tmp = travel[i]
	delta_p = abs(tmp[1] - pos[1]) + abs(tmp[2] - pos[2])
	delta_t = tmp[0] - pos[0]
	if delta_t < delta_p or (delta_t % 2 != delta_p % 2):
		print('No')
		break
	else:
		pos = tmp
else:
	print('Yes')