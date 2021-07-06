file=open('in1_20878977.txt','r')
print(file.read(11))

print(file.readline()) # starts reading where it lasted in previous read op

print(file.read())