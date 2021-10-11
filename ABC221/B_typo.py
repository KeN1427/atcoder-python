"""
B - typo

problem: https://atcoder.jp/contests/abc221/tasks/abc221_b
"""

S = list(input())
T = list(input())

for i in range(len(S)-1):
	if S[i] != T[i]:
		S[i] , S[i+1] = S[i+1], S[i]
		break
if S == T:
	print('Yes')
else:
	print('No')