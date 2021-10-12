"""
ABC049C - 白昼夢
problem: https://atcoder.jp/contests/abs/tasks/arc065_a
"""

s = input().replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
if s:
	print('NO')
else:
	print('YES')