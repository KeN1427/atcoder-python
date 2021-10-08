"""
C - AtCoderプログラミング講座

problem: https://atcoder.jp/contests/abc003/tasks/abc003_3
"""
N, K = map(int, input().split())
rates = list(map(int, input().split()))

rates.sort(reverse=True)
watchable = rates[:K]
watchable.sort()
result = 0
for rate in watchable:
	result = (result + rate) / 2
print(result)