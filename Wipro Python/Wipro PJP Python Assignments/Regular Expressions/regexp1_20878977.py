import re
file=open('reg1_20878977.txt','r')
flag=""

stri=file.readlines()

for x in stri:
    
    if re.match("192.168.10.12",x):
        flag="True"
    
if flag=="True":
    print("Pattern Found")
else:
    print("Pattern Not Found")
