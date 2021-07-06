file=open('in1_20878977.txt','r')
print("Reading line by line")
print()
count=0
for line in file:
    count += 1
    print( line.strip())
file.seek(0)
print("reading whole content!!!!")
print()
print(file.read())