## Lesson 41

Currently, spaces get encrypted as `'c'`. To maintain the original spacing in the plain message, you'll require a conditional `if` statement. This is composed of the `if` keyword, a condition, and a colon `:`.

Example Code

```python
if x != 0:
   print(x)
```

In the example above, the condition of the `if` statement is `x != 0`. The code `print(x)`, inside the `if` statement body, runs only when the condition evaluates to `True` (in this example, meaning that `x` is different from zero).

At the top of your for loop, replace `print(char == ' ')` with an `if` statement. The condition of this `if` statement should evaluate to `True` if `char` is an empty space and `False` otherwise. Inside the if body, print the string `'space!'`. Remember to indent this line.
