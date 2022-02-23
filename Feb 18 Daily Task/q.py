q=int(input("Enter the quantity : "))
if q*100 > 1000:
  print ("Cost is",((q*100)-(0.1*q*100)))
else:
  print ("Cost is",q*100)