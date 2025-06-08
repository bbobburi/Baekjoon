import sys

num = int(sys.stdin.readline())
for i in range(1, num+1):
    a, b = map(int, input().split())
    print("Case #"+str(i)+':',a, "+", b, "=", a+b)
