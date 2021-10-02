"""
ABC087B - Coins

problem: https://atcoder.jp/contests/abs/tasks/abc087_b
"""
a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0

for i in range(a + 1):
	if 500 * i == x:
		count += 1
		continue
	for j in range(b + 1):
		if 500 * i + 100 * j == x:
			count += 1
			continue
		for k in range(c + 1):
			if 500 * i + 100 * j + 50 * k == x:
				count += 1

print(count)
