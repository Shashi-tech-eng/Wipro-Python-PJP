def HyphenSort(str):
   li=str.split('-')  
   li.sort() 
   st=""
   for nm in li:
      st=st+nm
      st=st+" "
   
   st=st.strip()
   s=st.replace(" ","-")
   print(s)



line=input("Enter a string seperated by hyphen :")
HyphenSort(line)