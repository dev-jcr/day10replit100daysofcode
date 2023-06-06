myBill = float(input("What was the bill?: "))
tip = int(input("What % of tip from the bill you want to give?"))
numberOfPeople = int(input("How many people?: "))
tip = (tip / 100) * myBill
myBill = tip + myBill
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)