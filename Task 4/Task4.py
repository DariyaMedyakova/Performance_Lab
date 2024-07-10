import sys


with open(sys.argv[1]) as f:
    data = f.read().splitlines()
f.close()

num = []
for el in data:
    num.append(int(el))
num.sort()

countStep = 0
LenNum = len(num)
for i in range(0, LenNum // 2):
    countStep = countStep + (num[LenNum - i - 1] - num[i])
print(countStep)
