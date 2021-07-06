num1_20878977=int(input())
num2_20878977=int(input())

try:
   c=num1_20878977//num2_20878977
   # WE get Zer Division Error
except ZeroDivisionError:
   print("Divide by zero error")
else:
   print("Result ",c)