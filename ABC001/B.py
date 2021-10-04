"""
B - 視程の通報

problem: https://atcoder.jp/contests/abc001/tasks/abc001_2
"""

m = int(input())

km = m / 1000
vv = 0
if km < 0.1:
	vv = 0
elif 0.1 <= km and km <= 5:
	vv = int(km * 10)
elif 6 <= km and km <= 30:
	vv = int(km + 50)
elif 35 <= km and km <= 70:
	vv = int((km - 30) / 5 + 80)
else:
	vv = 89

if vv // 10 == 0:
	print('0' + str(vv))
else:
	print(vv)