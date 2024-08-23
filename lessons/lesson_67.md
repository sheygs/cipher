### Lesson 67

At the moment, your function prints some strings, but these values cannot be used by other parts of code to perform any actions.

For that purpose, you need to use a `return` statement:

Example Code

```python
def foo():
    return 'spam'
```

You need to write `return` followed by a space and the value that the function should return. Once the `return` statement is found, that value is returned and the execution of the function stops, proceeding to the next line of code after the function call. In the example above, the `foo` function returns the string `'spam'`.

Remove the two `print()` calls from your function and return `encrypted_text`.
