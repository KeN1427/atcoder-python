"""
E - Knapsack2
problem: https://atcoder.jp/contests/dp/tasks/dp_e
reference: https://kyopro-friends.hatenablog.com/entry/2019/01/12/230931
"""

DP_SIZE = 100001

N, W = map(int, input().split())
w = [0] * (N+1)
v = [0] * (N+1)
for i in range(N):
	w[i+1], v[i+1] = map(int, input().split())

dp = [[float('inf')] * DP_SIZE for i in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
	for j in range(DP_SIZE):
		if j - v[i] >= 0:
			dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i]] + w[i])
		else:
			dp[i][j] = dp[i-1][j]


ans = 100000
while dp[N][ans] > W:
	ans -= 1

print(ans)