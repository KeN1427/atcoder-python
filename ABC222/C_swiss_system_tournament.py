"""
C - Swiss-System Tournament

problem: https://atcoder.jp/contests/abc222/tasks/abc222_c
"""

N, M = map(int, input().split())
A = [input() for i in range(2*N)]
rank = [[i, 0] for i in range(2*N)]

def janken(player1, player2):
	if player1 == player2:
		return -1
	elif player1 == 'G' and player2 == 'P':
		return 1
	elif player1 == 'C' and player2 == 'G':
		return 1
	elif player1 == 'P' and player2 == 'C':
		return 1
	else:
		return 0

for i in range(M):
	for j in range(0, 2*N, 2):
		player1 = rank[j][0]
		player2 = rank[j+1][0]
		result = janken(A[player1][i], A[player2][i])
		if result != -1:
			rank[j+result][1] -= 1
	rank.sort(key=lambda x: (x[1], x[0]))

for i, _ in rank:
	print(i + 1)