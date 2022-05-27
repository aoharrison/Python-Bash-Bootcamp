# Variables

While we could continue doing math problems and printing silly statements, python has a lot of other uses.  One of the keys to python (and most other programming languages) is storing information in variables. 

## Assigning variables

The syntax for storing something as a variable in python is `variable_name = value`.  For an example, let's assign a the value of 5 and b the value of 3:

```python
>>> a=5
>>> b=3
```

Note that there will be no output from the interpreter this time as we did not "ask" it to return anything.  If you want to make sure your variables got assigned properly, just type the variable itself and hit `enter`:

```python
>>> a
5
>>> b
3
```

Note that you can overwrite variables:

```python
>>> a=6
>>> a
6
```

When we reassign a as 6, it loses its value as 5.  This is always an important thing to keep in mind when writing scripts and programs.

Variables can also have longer, more descriptive names and the value can be something other than an integer.  Here are a few examples:

```python
>>> height_inches = 72
>>> height_feet = 6
>>> height_conversational = 'six feet'
>>> height_all = (72, 6, 'six feet')
```

Notice that all of these variables names have multiple words and not all of the values are variables.  We will get into data types in the next lesson, so we won't worry about naming them now.

For variables with multiple words, I generally prefer to use underscores to show separation.  However, other people sometimes prefer using capitalization to show word breaks:

```python
>>> HeightInches = 72
>>> HeightFeet = 6
>>> HeightConversational = 'six feet'
>>> HeightAll = (72, 6, 'six feet')
```

Either convention is fine, but you're more likely to see the first used in python programming.

### Naming rules

One big rule to keep in mind is that variable names cannot begin with numbers.  Here are a few examples of invalid variable names:

```python
>>> 1 = a
  File "<stdin>", line 1
    1 = a
    ^
SyntaxError: cannot assign to literal
>>> 1 = 2
  File "<stdin>", line 1
    1 = 2
    ^
SyntaxError: cannot assign to literal
>>> 1a = 6
  File "<stdin>", line 1
    1a = 6
     ^
SyntaxError: invalid syntax
```

Another rule is that they cannot contain most special characters, as they have meaning to python.  Here are some more invalid variable names:

```python
>>> .2 = 8
  File "<stdin>", line 1
    .2 = 8
    ^
SyntaxError: cannot assign to literal
>>> .apple = banana
  File "<stdin>", line 1
    .apple = banana
    ^
SyntaxError: invalid syntax
>>> / = 0
  File "<stdin>", line 1
    / = 0
    ^
SyntaxError: invalid syntax
>>> g/h = k
  File "<stdin>", line 1
    g/h = k
    ^
SyntaxError: cannot assign to operator
>>> apple. = banana
  File "<stdin>", line 1
    apple. = banana
           ^
SyntaxError: invalid syntax
```

## Using variables

Now that we have assigned values to a and b, let's do some more simple math to get the hang of using the variables.  We'll perform the same operations as before, but with the variables instead of the numbers.

```python
>>> a + b
9
>>> a - b
3
>>> a * b
18
>>> a / b
2.0
```

We have different answers this time, but only because we're using different values.  For a little bit of craziness, we can assign the result of an operation to a variable.  For example:

```python
>>> c = a*b
>>> c
18
```

We can also put variables inside of functions.  I didn't mention this in the last lesson, but `print()` is a function, and we'll use it again here:

```python
>>> print('I am', height_conversational, 'tall')
I am six feet tall
```

There are other, better ways to insert variables into print statements that you will see along the way, but this will do for now.

## Exiting the Interpreter

You may be wondering why I haven't shown you how to quit the interpreter until now.  That's because I want you to see what happens to the variables when we do.

To close out of the interpreter, type `exit()`

```bash
>>> exit()
~ $
```

This will bring you back out to your default shell.  Now, let's relaunch the interpreter.  Remember that on Windows you should type `python` and on MacOS and Linux you should type `python3`.

```python
~ $ python3
Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Once you have the interpreter open again, try to get the value of `a`.

```python
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```

Now, requesting the value of a gets an `NameError` telling you that `'a' is not defined`.

What happened to `a` when we quit the interpreter?

## Scope

Scope essentially refers to when and where you can call a variable.  When you quit the interpreter, you are telling python you are done playing around for now and python deletes the variables from memory.  This is very useful because you don't have to worry about taking up memory with variables you assigned months ago.

Essentially the same thing happens when you are running python scripts; when a script is finished or when there are no remaining references to a variable within a script, the variable "falls out of scope" and is deleted.  In a script, this is referred to as [garbage collection](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)).  

The concept of scope can be tricky and we will not be covering it in this bootcamp, but you can check out [this article](https://realpython.com/python-scope-legb-rule/) if you're interested.
