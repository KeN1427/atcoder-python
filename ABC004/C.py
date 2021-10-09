"""
C - 入れ替え

problem: https://atcoder.jp/contests/abc004/tasks/abc004_3
"""

N = int(input())
cards = ['1', '2', '3', '4', '5', '6']

N %= 30

for i in range(N):
	m = i % 5
	cards[m], cards[m + 1] = cards[m + 1], cards[m]

print(''.join(cards))

	
