"""
A - Seismic magnitude scales
problem: https://atcoder.jp/contests/abc221/tasks/abc221_a
"""

A, B = map(int, input().split())

print(32 ** (A - B))