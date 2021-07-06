num1_20878977=input()
num2_20878977=input()
# DONE BY CODE WITH SV
 #We get TypeError
try:
    sub1_20878977=num2_20878977-num1_20878977
    print(sub1_20878977)
except TypeError:
    print("Convert strings to Numbers and subtract")
else:
    print(sub1_20878977)
finally:
    print("Subtraction Done")