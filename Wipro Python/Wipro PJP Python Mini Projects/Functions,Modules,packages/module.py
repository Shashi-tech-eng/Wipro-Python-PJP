def ispalindrome(name):
  
  
  if name == name[::-1]:
       print("Yes it is a palindrome")
  else:
       print("No it is not palindrome")



def count_the_vowels(name):
    sum=0
    for alpha in name.lower():
       if alpha in "aeiou":
           sum+=1
    print("No of vowels are: ",sum)



def frequency_of_letters(name):
   f={}
   for char in name:
      if char in f:
         f[char] +=1
      else:
         f[char] = 1
   
   print ("frequency of letters :")
   for k in f:
     if k!=" ":
        print(k,"-",f[k],end=" ")   