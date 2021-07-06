import sys
sum=0
print(sys.argv[1],sys.argv[3])
print(sys.argv[0])
print(len(sys.argv))
for i in range(1,len(sys.argv)):
    sum+=int(sys.argv[i])
print(sum)