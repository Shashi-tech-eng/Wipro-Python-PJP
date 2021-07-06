file=open('in1_20878977.txt','rb')
print(file.tell()) # output is 0
file.seek(0)
print(file.read(11).decode('utf-8'))
file.seek(-11,2)
print(file.read(11).decode('utf-8'))
print(file.tell())
file.seek(0)
print(file.tell())
