# Let's split the bill


Did you have fun messing with those mathematical symbols? Now let's put them to good use.

You and your friends went to dinner and need to split the bill. Being the clever friend you are, you can use your code to discover how much each person owes. (Remember, `myBill` is a float because the total bill will probably have a decimal point and `numberOfPeople` is an `int` because you did not go to dinner with .7 of a person.)

👉 Copy this code and see what happens:

```python
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
print("You all owe", answer)
```
Did you get a *really* funky number with sooo many decimal points?

&nbsp;

You can take your answer and use `round`. Round has two components: "What am I rounding?" and "How many decimal places am I rounding to?"

Add this portion of code after `answer` and before `print`. This shows you are rounding `answer` to 2 decimal points.

```python
answer = round(answer, 2)
```

