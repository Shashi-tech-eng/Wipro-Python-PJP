import sys

a=sys.argv[1]
b=sys.argv[2]
c=sys.argv[3]

list_1=a.split('-')
list_2=b.split('-')
list_3=c.split('-')

count=0

al=len(list_1)
bl=len(list_2)


for i in range(0,al,1):
   if list_1[i] in list_3:
      count+=1

for j in range(0,bl,1):
   if list_2[j] in list_3:
       count-=1

print(count)