"""
C -  直訴

problem: https://atcoder.jp/contests/abc002/tasks/abc002_3
"""

xa, ya, xb, yb, xc, yc = map(int, input().split())

xb, yb = xb - xa, yb - ya
xc, yc = xc - xa, yc - ya
xa, ya = 0, 0

area = abs(xb * yc - yb * xc) / 2

print(area)