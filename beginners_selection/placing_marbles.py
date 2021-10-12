"""
ABC081A - Placing Marbles
problem: https://atcoder.jp/contests/abs/tasks/abc081_a
"""

lst = list(map(int, input()))
count = 0
for i in lst:
	if i == 1:
		count += 1

print(count)
