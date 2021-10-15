"""
C - 風力観測
problem: https://atcoder.jp/contests/abc001/tasks/abc001_3
"""

from decimal import Decimal, ROUND_HALF_UP

Deg, Dis = map(int, input().split())

Dir = ''
W = 0
if Deg < 112.5:
	Dir = 'N'
elif Deg < 337.5:
	Dir = 'NNE'
elif Deg < 562.5:
	Dir = 'NE'
elif Deg < 787.5:
	Dir = 'ENE'
elif Deg < 1012.5:
	Dir = 'E'
elif Deg < 1237.5:
	Dir = 'ESE'
elif Deg < 1462.5:
	Dir = 'SE'
elif Deg < 1687.5:
	Dir = 'SSE'
elif Deg < 1912.5:
	Dir = 'S'
elif Deg < 2137.5:
	Dir = 'SSW'
elif Deg < 2362.5:
	Dir = 'SW'
elif Deg < 2587.5:
	Dir = 'WSW'
elif Deg < 2812.5:
	Dir = 'W'
elif Deg < 3037.5:
	Dir = 'WNW'
elif Deg < 3262.5:
	Dir = 'NW'
elif Deg < 3487.5:
	Dir = 'NNW'
else:
	Dir = 'N'


d = Decimal(Dis) / Decimal(60)
ws = float(d.quantize(Decimal('0.0'), rounding=ROUND_HALF_UP))

if ws <= 0.2:
	Dir = 'C'
	W = 0
elif ws <= 1.5:
	W = 1
elif ws <= 3.3:
	W = 2
elif ws <= 5.4:
	W = 3
elif ws <= 7.9:
	W = 4
elif ws <= 10.7:
	W = 5
elif ws <= 13.8:
	W = 6
elif ws <= 17.1:
	W = 7
elif ws <= 20.7:
	W = 8
elif ws <= 24.4:
	W = 9
elif ws <= 28.4:
	W = 10
elif ws <= 32.6:
	W = 11
else:
	W = 12

print(Dir, W)