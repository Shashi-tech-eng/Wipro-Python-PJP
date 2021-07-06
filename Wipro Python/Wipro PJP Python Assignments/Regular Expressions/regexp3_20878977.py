import re
file=open('reg1_20878977.txt','r')
flag=""
repl=""
stri=file.readlines()

for x in stri:
    
    if re.match("CIS",x):
        flag="True"
        repl=x

    
if flag=="True":
    re.sub("CIS","UNIX",repl)
    print("Pattern Substitutuion Done")
else:
    print("Pattern Substitutuion Not Done")
        