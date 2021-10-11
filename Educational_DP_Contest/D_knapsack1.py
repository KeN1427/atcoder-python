"""
D - Knapsack1

problem: https://atcoder.jp/contests/dp/tasks/dp_d
"""

N, W = map(int, input().split())
w = [0] * N
v = [0] * N
for i in range(N):
	w[i], v[i] = map(int, input().split())


dp = [[0] * (W + 1) for i in range(N)]
for i in range(N):
	for j in range(W + 1):
		if j - w[i] >= 0:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
		else:
			dp[i][j] = dp[i-1][j]

print(dp[N-1][W])