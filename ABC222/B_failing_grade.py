"""
B - Failing Grade

problem: https://atcoder.jp/contests/abc222/tasks/abc222_b
"""

N, P = map(int, input().split())
points = list(map(int, input().split()))
result = 0

for p in points:
	if p < P:
		result += 1

print(result)