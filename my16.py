n = int(input())
print(n//3600,str(n//60%60//10) + str(n//60%60%10),str(n%60//10) + str(n%60%10), sep = ':')