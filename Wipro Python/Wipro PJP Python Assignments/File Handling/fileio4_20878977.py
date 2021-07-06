file=open('newfile1_20878977.txt','r')
# If this file is not there in current working directory we get "No such file or directory: 'newfile1_UserID.txt'"
file=open('newfile_20878977.txt','w')
# If this file is not there in current working directory and open in write format we dont get any output on console
file=open('newfile_20878977.txt','w+')
s1_20878977="This is the newline added at end"
file.write(s1_20878977)
file.seek(0)
print(file.read()) # used access mode w+ to read and write as well
file.close()