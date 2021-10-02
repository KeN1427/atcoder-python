"""
ABC088B - Card Game for Two

problem: https://atcoder.jp/contests/abs/tasks/abc088_b
"""

n = int(input())
cards = list(map(int, input().split()))


alice = 0
bob = 0

while len(cards):
	alice += cards.pop(cards.index(max(cards)))
	if len(cards):
		bob += cards.pop(cards.index(max(cards)))

print(alice - bob)