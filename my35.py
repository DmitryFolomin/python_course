import math
L, W, H = map(int,input().split())
print(math.ceil(((L + W)*H)/8))