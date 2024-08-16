n = int (input())
k_100 = n // 100
n = n % 100
k_20 = n // 20
n = n % 20
k_10 = n // 10
n = n % 10
k_5 = n // 5
n = n % 5
k_1 = n // 1
d = k_100 + k_20 + k_10 + k_5 + k_1
print (d)