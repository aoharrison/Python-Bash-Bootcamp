# Introduction to Python

## What is python?

Python first came on the scene in [1989](https://en.wikipedia.org/wiki/History_of_Python) and was named after the TV show [Monty Python's Flying Circus](https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus).  It started becoming popular in the ealry 2000s and currently ranks as the [most popular programming language](https://www.tiobe.com/tiobe-index/).  It has become very popular in scientific research including in bioinformatics and computational biology and chemistry as well as in data science.

Python is a [high-level](https://en.wikipedia.org/wiki/High-level_programming_language) programming language.  This means that when working with python, we are not directly commanding the details of the computer (e.g., bits and bytes).  Instead, we will be working in more abstract terms (as far as the computer is concerned) that will be more familiar to us humans.


## Interacting with python: The python interpreter

This is the most basic way to interact with python and in some ways may feel similar to using the command line: put in one argument at a time and get one result back.  Later on, we will be using Jupyter notebooks and scripts.

### Launch the interpreter

To launch the interpreter, follow the instructions for your operating system below:

*Note: This step will not work if you have not installed python.*

**Windows**

Open the command prompt.  The easiest way is to click the `Start` button, type "cmd" into the search bar, and select the program called "Command Prompt."

After launching the command prompt, type:

```
python
```

and hit the `enter` key.  If this doesn't work, try just `py` instead of `python`.

**MacOS**

Open your terminal.  You can do this either by going to `Applications/Utilities` in the Finder and double clicking on its icon or by using Spotlight to search for the application `Terminal`.

After launching your terminal, type:

```
python3
```

and hit the `enter` key.

**Linux**


Open your terminal.  The easiest way to do this is to search for an application called “terminal”, “command”, “prompt” or “shell”.

After launching your terminal, type:

```
python3
```

and hit the `enter` key. 


### Using the interpreter

If you were able to launch the interpreter, your terminal should now be showing you something that looks like this:

```
~ $ python3
Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` is the prompt where you will be typing in code.  To use the interpreter, all you need to do is type something out after the prompt and hit `enter`!  We'll demonstrate this with some math problems first.  

Type each of these in and make sure you get the same answers as are shown:

```python
>>> 5 + 3
8
>>> 5 - 3
2
>>> 5 * 3
15
>>> 5 / 3
1.6666666666666667
```

And that's how it's done!  A useful tip is that you can search through past commands using the `up arrow` key.  Try it out now.

Before we move on, let's do one more thing: print a statement to the screen.  This first example is very simple, but we will build on it later. 

```python
>>> print("Python is fun!")
Python is fun!
```

Note that if you forget to close the parentheses at the end, you will get an ellipse (`. . .`) telling you that the statement isn't closed.  Just type a `)` to appease python.

```python
>>> print("Python is fun!"
... )
Python is fun!
```
