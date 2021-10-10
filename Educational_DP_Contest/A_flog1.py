"""
A - Frog1

problem: https://atcoder.jp/contests/dp/tasks/dp_a
"""

N = int(input())
H = list(map(int, input().split()))
dp = [0] * (N)

for i in range(1, N):
	if i - 2 >= 0:
		dp[i] = min(dp[i - 1] + abs(H[i - 1] - H[i]), dp[i - 2] + abs(H[i - 2] - H[i]))
	else:
		dp[i] = dp[i - 1] + abs(H[i - 1] - H[i])

print(dp[N-1])