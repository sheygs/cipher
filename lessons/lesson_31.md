### Lesson 31

When you try to change the individual characters of a string as you did in the previous step, you get a `TypeError`, which occurs when an object of inappropriate type is used in your code.

As you can see from the error message, strings do not support item assignment, because they are immutable. However, a variable can be reassigned another string:

```python
message = 'Hello World'
message = 'Hello there!'
```

Delete the `text[0]` line and reassign `text` the string `'Albatross'`.
