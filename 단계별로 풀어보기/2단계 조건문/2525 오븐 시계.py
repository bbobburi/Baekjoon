H, M = map(int, input().split())
time = int(input())

H += time//60
M += time%60

if M >= 60:
    H += 1
    print(H%24, M-60)
else:
    print(H%24, M)
