"""
B - AtCoderoトランプ

problem: https://atcoder.jp/contests/abc003/tasks/abc003_2
"""

S = input()
T = input()

for i in range(len(S)):
	if S[i] == T[i]:
		continue
	elif S[i] == '@' and T[i] in 'atcoder':
		continue
	elif T[i] == '@' and S[i] in 'atcoder':
		continue
	else:
		print('You will lose')
		break
else:
	print('You can win')