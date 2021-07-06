num1_20878977=int(input())
#sum1_20878977=num1_20878977+num2_20878977
#print(sum1_20878977)
# We get NameError as Output
try:
    sum1_20878977=num1_20878977+num2_20878977
except NameError:
    print("Please declare another Variable to perform sum")
    