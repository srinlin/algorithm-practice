H, M = map(int, input().split())
T = (H*60 + M -45)
if T//60 < 0:
    print(T//60 +24, T%60, end = ' ')
else:
    print(T//60 ,T%60, end = ' ')