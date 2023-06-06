# 👉 Day 10 Challenge

## Extend your bill calculator

Add a tip function that adds the total tip to the bill before splitting it equally between the people.

 

1. Ask the user for the total bill amount.
2. Ask what % of tip they will leave to be added to the bill total.
<details> <summary> 💡 Hint </summary>

Typically, a tip is either 15%, 18% or 20% of the total bill.</details>

3. Figure out how to get the total bill with tip then add that to original amount.
 
 <details> <summary> 💡 Hint  </summary>
Divide the tip percentage by 100, and multiply that to the total bill amount BEFORE adding that to the original amount.
</details>

4. Ask the user how many people are splitting the bill and divide by the total.

You can use the same code to get started:

```python
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
print("You all owe", answer)
```

