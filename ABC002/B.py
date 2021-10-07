"""
B -  罠

problem:https://atcoder.jp/contests/abc002/tasks/abc002_2
"""

W = input()
trap = 'aiueo'

for i in range(len(trap)):
	W = W.replace(trap[i], '') 

print(W)