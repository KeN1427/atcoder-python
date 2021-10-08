"""
B - 回転

problem: https://atcoder.jp/contests/abc004/tasks/abc004_2
"""

c0 = list(input().split())
c1 = list(input().split())
c2 = list(input().split())
c3 = list(input().split())

lst = [c3, c2, c1, c0]
for c in lst:
	print(c[3], c[2], c[1], c[0])