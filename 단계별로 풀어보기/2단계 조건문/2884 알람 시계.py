time, minute = map(int, input().split())

if minute >= 45:
    print(time, minute - 45)
else:
    if time == 0:
        print(23, minute + 15)
    else:
        print(time - 1, minute + 15)
