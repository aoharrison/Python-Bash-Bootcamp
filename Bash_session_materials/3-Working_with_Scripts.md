# Working with Scripts

In addition to being a shell, bash is also a scripting language.  This means that we can write files full of bash script and execute them all together.  We are going to write a script that combines all of the squirrel data into one large data table and then use it to answer these questions:

1. How many total squirrels were observed in NYC parks?
2. How many squirrels were observed in each park?
3. How many squirrels with each color combination (primary color + highlights) were observed?

Most of the code will be familiar by now, but we will introduce one new topic: the [for loop](https://www.cyberciti.biz/faq/bash-for-loop/).  

## For Loops

For loops show up in virtually all languages and are incredibly useful.  What they allow you to do is perform the same task on multiple files or other objects without needing to write out separate code for each task.  The basic syntax for a for loop in bash is:

```bash
for i in 1 2 3 4 5
do
   echo "Welcome $i times"
done
```

The above syntax is for a script.  On the command line it would be:

```bash
for i in 1 2 3 4 5; do echo "Welcome $i times";done
```

Notice that we have replaced two of the carriage returns with `;`.  Let's run the command line version and see the results.

```bash
bash_bootcamp $ for i in 1 2 3 4 5; do echo "Welcome $i times";done
Welcome 1 times
Welcome 2 times
Welcome 3 times
Welcome 4 times
Welcome 5 times
```

As you can see, we printed "Welcome" a total of 5 times.  In a for loop, we say that for each item provided (in this case the numbers 1 through 5), do some sort of task.  A for loop always performs the task on the items in the order that they are provided.  The syntax `for i` stores each of the items as the variable `i` during its time in the loop.  We can see this variable being called in the `do` portion of the statement using `$i`.  Remember when we rane `echo $HOME` at the very beginning?  Well, this is very similar.  We are again using `echo` to print the value of a variable.

## Writing a Script

We are going to use a program called `nano` to write our script.  It's good for teaching because it displays your options on the screen for you.  Note, however, that there can sometimes be issues using `nano` (and other command line text editors) with Windows Subsystem for Linux.  You should still try it out, but we can also provide you with the script if you have trouble creating it.  Just send a message.

First, we'll create the file.  Let's call it `squirrel_script.sh` (`.sh` is the standard file extension for bash):

```bash
bash_bootcamp $ touch squirrel_script.sh
bash_bootcamp $ ls -l
total 16
-rw-r--r--   1 ameliaharrison  staff  550 May 31 21:40 all_parks_list.txt
drwxr-xr-x@  3 ameliaharrison  staff   96 May 31 15:54 park_data
-rw-r--r--   1 ameliaharrison  staff  403 May 31 21:40 parks_with_squirrels.txt
drwxr-xr-x@ 10 ameliaharrison  staff  320 May 31 21:17 squirrel_data
-rw-r--r--   1 ameliaharrison  staff    0 May 31 22:06 squirrel_script.sh
```

The touch command is used mainly to modify timestamps on files, but it will also create a file if it does not already exist.  Notice that `squirrel_script.sh` is empty (it contains 0 bytes).  

Now, let's open the file up for editing:

```bash
bash_bootcamp $ nano squirrel_script.sh
```

You will get a screen that looks something like this, but with highlighting:

```bash
  GNU nano 2.0.6            File: squirrel_script.sh












^G Get Help   ^O WriteOut   ^R Read File  ^Y Prev Page  ^K Cut Text   ^C Cur Pos
^X Exit       ^J Justify    ^W Where Is   ^V Next Page  ^U UnCut Text ^T To Spell
```

The first thing we will do in our script is make a new directory to store our new squirrel dataset in.  Let's call it `all_squirrels_combined.txt` to differentiate it from our last big squirrel set.  Type or paste the following into your `nano` file, including the line that starts with `#`:

```bash
# make a new directory to store the data
mkdir combined_squirrel_data
```

`#` goes by many names, including hashtag, pound sign, and octothorpe (my personal favorite).  In many languages, it indicates that a line is a comment rather than a command.  Functionally, it allows you to annotate your code by telling bash "this line is not code and you should not try to run it."

Before we get further, let's practice quitting and saving.  To exit, hit `^X` as indicated in the bottom left corner.  You will get a message asking if you want to `Save modified buffer (ANSWERING "No" WILL DESTROY CHANGES) ?`.  Hit `y` for yes.  Then, it will ask you if you want to write to the same file name you entered: `File Name to Write: squirrel_script.sh`.  Hit `enter` or `return` to get past this message.  Now that we know how to do that, type `nano squirrel_script.sh` again to get back into the script.  

Next, we need to make the big file again, but I promised to show you another way.  This is where the for loop comes in.  Paste this text into your script, underneath the part where you make the directory:

```bash
# combine the single park files into one big squirrel file
## take the header from one park file and put it into the new file
head -1 squirrel_data/central_manhattan/madison_square_park_squirrels.txt > combined_squirrel_data/all_squirrels_combined.txt

## for each single park file, remove the first row and add it to the end of the big squirrel file
for f in squirrel_data/*/*_park_squirrels.txt
do
  sed 1d "$f" >> combined_squirrel_data/all_squirrels_combined.txt
done
```

This looks scary, but you've seen most of it before.  Remember how I said another solution to the multiple header lines was to not put them into the file in the first place?  This block of code solves the problem.  First, because we do want one header line, we need to grab one and put it into a file.  I chose Madison Square Park at random, but any one would do.  Next, we have our for loop.  We use the variable name `f` for "file" and then tell it that the items we want it to loop through are the squirrel data files for the individual parks (remember the globs?).  Then, for each file, we use `sed` to remove the very first line (the header).  Finally, we use the double pipe `>>` (I told you we would see it later) to add the file contents to the end of the new big squirrel file.  That way, we don't overwrite the data currently in there.

Now we will have made our big file and we can get around to answering the questions:

1. How many total squirrels were observed in NYC parks?
2. How many squirrels were observed in each park?
3. How many squirrels with each color combination (primary color + highlights) were observed?

Underneath the code you already have, add these lines:

```bash
# count the number of squirrels in the new file
echo "----------------------------------------------------------------------"
printf "1. How many total squirrels were observed in NYC parks?\n\n"
printf "Total number of squirrels observed in NYC parks:\n\n"
sed 1d combined_squirrel_data/all_squirrels_combined.txt | wc -l

# count the number of squirrels from each park
echo "----------------------------------------------------------------------"
printf "2. How many squirrels were observed in each park?\n\n"
printf "The number of squirrels in each park:\n\n"
sed 1d combined_squirrel_data/all_squirrels_combined.txt | cut -f3 | sort | uniq -c

# number of squirrels with each color combination
echo "----------------------------------------------------------------------"
printf "3. How many squirrels with each color combination (primary color + highlights) were observed?\n\n"
printf "The number of squirrels observed with each color combination:\n\n"
sed 1d combined_squirrel_data/all_squirrels_combined.txt | cut -f6-7 | sort | uniq -c
```

Here, we use `echo` and `printf` to make the output a little prettier and hopefully easier to read.  You will see their utility when we run the script (notice the newlines `\n` that will space out our results).  The only other new things are that we've used `sed` on the files to remove the first line so that we can get an accurate count with `wc -l` and that for the fur color combo, we used `cut` to pull both the primary and highlight fur color columns.

Once you have all of these lines in your script, exit and save.

## Running a script

To run a script, type `bash` and then the name of the script into the command prompt and hit enter:

```bash
bash_bootcamp $ bash squirrel_script.sh
----------------------------------------------------------------------
1. How many total squirrels were observed in NYC parks?

Total number of squirrels observed in NYC parks:

     433
----------------------------------------------------------------------
2. How many squirrels were observed in each park?

The number of squirrels in each park:

cut: stdin: Illegal byte sequence
  26 Battery Park
  18 City Hall Park
   3 Columbus Park
  12 John V. Lindsay East River Park
  11 Madison Square Park
  44 McCarren Park
  14 Msgr. McGolrick Park
  25 Stuyvesant Square Park
  59 Tompkins Square Park
  16 Union Square Park
  51 Washington Square Park
----------------------------------------------------------------------
3. How many squirrels with each color combination (primary color + highlights) were observed?

The number of squirrels observed with each color combination:

cut: stdin: Illegal byte sequence
   5 Black	Black
   6 Black	Cinnamon
   5 Cinnamon	Cinnamon
   1 Cinnamon	Gray
   1 Cinnamon	Gray, Cinnamon
   2 Cinnamon	Gray, White
   9 Cinnamon	NA
   6 Cinnamon	White
   1 Gray
   1 Gray	Black
  39 Gray	Cinnamon
  18 Gray	Cinnamon, White
  80 Gray	Gray
  74 Gray	NA
  30 Gray	White
   1 NA	NA
```

If you have everything correct, the above output is what you should see.  Notice that we are getting a warning message: `cut: stdin: Illegal byte sequence`.  This means that somewhere in our table we have one or more characters that is not UTF-8 encoded (basically, anything you don't see on your keyboard right now).  For our purposes now, this is not really an issue, but just another example of the importance of data cleaning!

# Conclusions

In this lesson, you learned how to write and run scripts, and how to write for loops.  

During today's bootcamp, you learned many valuable commands to get you going on the command line immediately with respect to data analysis. 

Happy coding!