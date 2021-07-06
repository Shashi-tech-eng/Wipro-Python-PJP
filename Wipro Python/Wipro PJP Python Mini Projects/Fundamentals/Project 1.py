km=int(input("How far would you like to travel in miles?"))

if km<3:
  print("I suggest Bicycle to your destination")
elif km>3 and km<300:
  print("I suggest Motor-Cycle to your destination")
else:
  print("I suggest Super-Car to your destination")