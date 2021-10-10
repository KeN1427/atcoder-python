"""
B - flog2

problem: https://atcoder.jp/contests/dp/tasks/dp_b
* PyPy3
"""

N, K = map(int, input().split())
H = list(map(int, input().split()))
dp = [0] * (N)

for i in range(1, N):
	dp[i] = dp[i - 1] + abs(H[i - 1] - H[i])
	for j in range(2, K + 1):
		if i - j >= 0:
			dp[i] = min(dp[i], dp[i - j] + abs(H[i - j] - H[i]))

print(dp[N-1])