"""
D - 感雨時刻の整理
problem: https://atcoder.jp/contests/abc001/tasks/abc001_4
"""

def rounder(num, attr):
	digit = num % 10
	result = num - digit
	if attr == 'start':
		if digit >= 5:
			result += 5
	else:
		if digit == 0:
			pass
		elif 0 < digit and digit <= 5:
			result += 5
		else:
			result += 10
			if result % 100 == 60:
				result = num - (num % 100) + 100
	return result
 
def to_str(num):
	return ('0' * (4 - len(str(num)))) + str(num)


memo = []
result = []
N = int(input())
for i in range(N):
	s, e = map(int, input().split('-'))

	s = rounder(s, 'start')
	e = rounder(e, 'end')

	memo.append([s, e])

memo.sort(key=lambda x: x[0])

for i in range(len(memo)):
	tmp_s = memo[i][0]
	tmp_e = memo[i][1]

	if i == 0:
		result.append([tmp_s, tmp_e])
	else:
		pre_s = result[-1][0]
		pre_e = result[-1][1]
		if tmp_s == pre_s or tmp_s <= pre_e:
			result[-1][1] = max(pre_e, tmp_e)
		else:
			result.append([tmp_s, tmp_e])

for lst in result:
	print(to_str(lst[0]) + '-' + to_str(lst[1]))

