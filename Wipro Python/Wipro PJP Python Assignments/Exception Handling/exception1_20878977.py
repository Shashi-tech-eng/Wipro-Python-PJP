#file=open('newfile1_20878977.txt','r')
# We get No such file or directory: 'newfile1_20878977.txt' File Not Found Error
try:
    file=open('newfile1_20878977.txt','r')
except FileNotFoundError:
    print("Cant Open This File")
finally:
    print("Please try again")