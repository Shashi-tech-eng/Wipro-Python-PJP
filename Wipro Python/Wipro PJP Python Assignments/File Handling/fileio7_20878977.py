file=open('in1_20878977.txt','rb')
print(file.read()[-11:].decode('utf-8'))
file.seek(-13, 1)
print(file.readline().decode('utf-8'))
file.seek(5,0)
print(file.readline().decode('utf-8'),end='')
print(file.tell())