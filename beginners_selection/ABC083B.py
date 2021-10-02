"""
ABC083B - Some Sums

problem: https://atcoder.jp/contests/abs/tasks/abc083_b
"""

n, a, b = map(int, input().split())
result = 0 

for i in range(1, n + 1):
	sum = 0
	tmp = i
	while tmp:
		sum += tmp % 10
		tmp //=  10
	if a <= sum and sum <= b:
		result += i

print(result)