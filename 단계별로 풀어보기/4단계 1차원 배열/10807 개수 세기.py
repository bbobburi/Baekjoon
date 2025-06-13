import sys

num = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
num2 = int(sys.stdin.readline())
print(lst.count(num2))
