"""
ABC081B - Shift only
"""
n = int(input())
lst = list(map(int, input().split()))

count = 0
flag = 1

while(flag):
	for i in range(n):
		if lst[i] % 2 == 0:
			lst[i] /= 2
		else:
			flag = 0
	count += flag

print(count)
