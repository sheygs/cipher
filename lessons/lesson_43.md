### Lesson 43

A conditional statement can also have an `else` clause. This clause can be added to the end of an `if` statement to execute alternative code if the condition of the `if` statement is false:

Example Code

```python
if x != 0:
   print(x)
else:
   print('x = 0')
```

As you can see in your output, when the loop iterations reach the space, a space is added to the encrypted string. Then the code outside the `if` block executes and a `c` is added to the encrypted string.

To fix it, add an `else` clause after `encrypted_text += char` and indent all the subsequent lines of code except the `print()` call.
