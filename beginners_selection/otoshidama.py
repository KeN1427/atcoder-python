"""
ABC085C - Otoshidama
problem: https://atcoder.jp/contests/abs/tasks/abc085_c
"""
n, y = map(int, input().split())

for i in range(n + 1):
	for j in range(n + 1 - i):
		k = (y - (i * 10000 + j * 5000))//1000 
		if i + j + k == n:
			print(f'{i} {j} {k}')
			exit()
else:
	print('-1 -1 -1')