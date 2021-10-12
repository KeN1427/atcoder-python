"""
ABC085B - Kagami Mochi
problem: https://atcoder.jp/contests/abs/tasks/abc085_b
"""

n = int(input())
lst = []
for i in range(n):
	lst.append(int(input()))

print(len(set(lst)))
