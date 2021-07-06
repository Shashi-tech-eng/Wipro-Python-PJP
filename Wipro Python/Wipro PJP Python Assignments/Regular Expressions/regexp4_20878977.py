import re
file=open('reg1_20878977.txt','r')
flag=""
stri=file.readlines()
for x in stri:
    for i in x.split(" "):
        if re.match("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",i):
            flag="True"
  
if flag=="True":
    print("Email ID Found")
else:
    print("Email ID Not Found")
