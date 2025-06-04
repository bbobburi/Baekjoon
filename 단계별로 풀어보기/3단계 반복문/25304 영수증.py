price = int(input())
num = int(input())
result = 0

for _ in range(num):
    a, b = map(int, input().split())
    result += a * b

if price == result:
    print("Yes")
else:
    print("No")
