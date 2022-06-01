# Working with Text Files

One of the reasons that bash and other shells rock is because they allow you to manipulate text files.  That sounds kind of lame, but researchers often have a ton of text data, especially tables.  This data almost always needs to be cleaned up and shuffled around before any computational analysis, even when using graphical systems like Excel or Google Sheets.  On the small scale, this is tedious and annoying.  On the large scale, this can become impossible to do by hand.  The manual way is also more prone to errors.

## Viewing files

There are a few ways to view files on the command line without going into your file browser and double-clicking.  Let's take a look at that `park_info.txt` file.

The first viewing option is `less`:

```bash
bash_bootcamp $ less park_data/park_info.txt
```

This sort of takes you away form the command line and into the file.  This view is the same as `man` earlier.  You should be able to scroll through the file using your mouse, trackpad, or arrow keys.  We can see that `park_info.txt` does in fact contain information about parks, specifically parks in New York City.  To quit the view, just hit `q`.

Now that we know about `park_info.txt`, let's check those squirrel datasets.  Move into the `squirrel_data/brooklyn` directory and take a look at `mccarren_park_squirrels.txt`.  What information is in this file?

You should see information about individual squirrels, including location, fur color, activities, etc. Go ahead and quit the `less` view.

While we're here, let's check out some other ways to look at files.  To print an entire file to the screen, we can use `cat`:

```bash brooklyn $ cat mccarren_park_squirrels.txt
Area.Name	Area.ID	Park.Name	Park.ID	Squirrel.ID	Primary.Fur.Color	Highlights.in.Fur.Color	Color.Notes	Location	Above.Ground..Height.in.Feet.	Specific.Location	Activities	Interactions.with.Humans	Other.Notes.or.Observations	Squirrel.Latitude..DD.DDDDDD.	Squirrel.Longitude...DD.DDDDDD.
BROOKLYN	D	McCarren Park	22	D-22-01	Cinnamon	White	NA	Ground Plane	NA	NA	Eating	Indifferent	NA	40.72167	-73.953364
BROOKLYN	D	McCarren Park	22	D-22-02	Gray	White	NA	Ground Plane	NA	NA	Eating	Approaches	NA40.721768	-73.953192
BROOKLYN	D	McCarren Park	22	D-22-03	Gray	White	NA	Ground Plane	NA	NA	Running	Runs From	Ran in from baseball field	40.721662	-73.953278
BROOKLYN	D	McCarren Park	22	D-22-04	Gray	Cinnamon	NA	Above Ground	NA	NA	Climbing	Runs From	NA	40.721857	-73.953139
BROOKLYN	D	McCarren Park	22	D-22-05	Cinnamon	NA	NA	Ground Plane	NA	NA	Running	ApproachesRunning around	40.721941	-73.952947
BROOKLYN	D	McCarren Park	22	D-22-06	Cinnamon	NA	NA	Above Ground	NA	NA	Climbing	Approaches	Perched up, came close to us!	40.722039	-73.952796
BROOKLYN	D	McCarren Park	22	D-22-07	Cinnamon	NA	NA	Ground Plane	NA	NA	Chasing	ApproachesSkinny tail, was in the baseball field	40.72147	-73.952857
BROOKLYN	D	McCarren Park	22	D-22-08	Cinnamon	White	NA	Ground Plane	NA	NA	Running	Runs FromNA	40.721713	-73.95305
BROOKLYN	D	McCarren Park	22	D-22-09	Gray	Gray	NA	Ground Plane, Specific Location	NA	In a trash and metal heap next to baseball field	Eating, Foraging	Indifferent	NA	40.721933	-73.953147
BROOKLYN	D	McCarren Park	22	D-22-10	Gray	Cinnamon, White	NA	Above Ground, Specific Location	12	in tree	Climbing	Runs From	Ran up a tree	40.722283	-73.953115
BROOKLYN	D	McCarren Park	22	D-22-11	Gray	Gray	NA	Ground Plane	NA	NA	Running	Runs From	Ran out of park	40.722698	-73.953198
BROOKLYN	D	McCarren Park	22	D-22-12	Gray	White	NA	Ground Plane	NA	NA	Eating, Foraging	Indifferent	Birds walking nearby	40.722819	-73.952095
BROOKLYN	D	McCarren Park	22	D-22-13	Gray	White	NA	Above Ground	NA	NA	Climbing	Indifferent	Ran from ground to tree	40.722966	-73.951987
BROOKLYN	D	McCarren Park	22	D-22-14	Cinnamon	White	NA	Above Ground, Specific Location	3	in short tree	Climbing, Sitting in short tree	Indifferent	NA	40.723136	-73.951794
BROOKLYN	D	McCarren Park	22	D-22-15	Gray	White	NA	Above Ground, Specific Location	NA	in tree	Eating	Indifferent	NA	40.723071	-73.951697
BROOKLYN	D	McCarren Park	22	D-22-16	Cinnamon	Gray	NA	Ground Plane, Specific Location	NA	below park benches	Foraging, Jumping	Indifferent	Great jumper	40.723006	-73.951655
BROOKLYN	D	McCarren Park	22	D-22-17	Gray	Cinnamon, White	NA	Above Ground	9	NA	Chilling	Indifferent	Perched on branch, just hanging out	40.722962	-73.951752
BROOKLYN	D	McCarren Park	22	D-22-18	Cinnamon	Cinnamon	NA	Above Ground	14	NA	Hanging	Indifferent	Perched on branch	40.722603	-73.951449
BROOKLYN	D	McCarren Park	22	D-22-19	Cinnamon	Gray, White	NA	Above Ground	20	NA	Running, Climbing	NA	Very small, climbed from one tree to another	40.721247	-73.951609
BROOKLYN	D	McCarren Park	22	D-22-20	Gray	Cinnamon, White	NA	Above Ground	75	NA	Climbing	Indifferent	Small, on tree on branch, two others below it	40.720606	-73.952769
BROOKLYN	D	McCarren Park	22	D-22-21	Gray	Cinnamon, White	NA	Above Ground	15	NA	Chasing, ClimbingIndifferent	Started in middle of tree, started chasing others up in branches, jumped from branch to branch	40.720582	-73.952694
BROOKLYN	D	McCarren Park	22	D-22-22	Gray	Cinnamon, White	NA	Above Ground	20	NA	Climbing	Indifferent	One of three together on a tree	40.720533	-73.95272
BROOKLYN	D	McCarren Park	22	D-22-23	Gray	White	NA	Above Ground	20	NA	Climbing	Indifferent	Jumped from one tree to next	40.720488	-73.952806
BROOKLYN	D	McCarren Park	22	D-22-24	Gray	White	NA	Ground Plane	NA	NA	Eating, Foraging	Indifferent	Dog chased it up a tree	40.720458	-73.954244
BROOKLYN	D	McCarren Park	22	D-22-25	Gray	Cinnamon, White	NA	Ground Plane	NA	NA	Foraging	Skittish to humans	NA	40.720018	-73.953442
BROOKLYN	D	McCarren Park	22	D-22-26	Gray	White	NA	Ground Plane	NA	NA	Running, Foraging	Indifferent	Fast	40.720026	-73.953652
BROOKLYN	D	McCarren Park	22	D-22-27	Gray	Cinnamon	NA	Ground Plane	NA	NA	Eating (bread crumbs), Foraging	Indifferent	Near a lot of little birds	40.719777	-73.952774
BROOKLYN	D	McCarren Park	22	D-22-28	Gray	White	NA	Ground Plane	NA	NA	Running	Indifferent	Running against fence	40.720114	-73.952768
BROOKLYN	D	McCarren Park	22	D-22-29	Gray	Cinnamon, White	NA	Ground Plane	NA	NA	Hanging out	Runs From	Standing at base of tree, then climbed up	40.719944	-73.952505
BROOKLYN	D	McCarren Park	22	D-22-30	Gray	White	NA	Ground Plane	NA	NA	Foraging	Indifferent	NA	40.720448	-73.952521
BROOKLYN	D	McCarren Park	22	D-22-31	Cinnamon	White	NA	Ground Plane	NA	NA	Foraging	Indifferent	Walking around bushes	40.720412	-73.952353
BROOKLYN	D	McCarren Park	22	D-22-32	Gray	Cinnamon, White	NA	Ground Plane	NA	NA	Foraging	Indifferent	A little on the robust side	40.720372	-73.952326
BROOKLYN	D	McCarren Park	22	D-22-33	Gray	Cinnamon	NA	Ground Plane	NA	NA	Foraging	Indifferent	Busy digging for something	40.720749	-73.951891
BROOKLYN	D	McCarren Park	22	D-22-34	Cinnamon	Cinnamon	NA	Above Ground	15	NA	Sleeping (Dead?)	Indifferent	It almost looks dead. Eyes open, curled up into itself in a nook in a tree with #35.	40.721181	-73.951255
BROOKLYN	D	McCarren Park	22	D-22-35	Cinnamon	Cinnamon	NA	Above Ground	15	NA	Sleeping (Dead?)	NA	Curled up together with #34. One big furry ball of squirrel.	40.721181	-73.951255
BROOKLYN	D	McCarren Park	22	D-22-36	Cinnamon	Gray, Cinnamon	Reddish tail	Ground Plane	NA	NA	Eating (tortilla/chip)	NA	Pretty fat	40.72112	-73.95104
BROOKLYN	D	McCarren Park	22	D-22-37	Gray	Gray	NA	Ground Plane	NA	NA	Running	Indifferent	Turning around, trying to eat	40.721315	-73.950943
BROOKLYN	D	McCarren Park	22	D-22-38	Gray	Cinnamon, White	NA	Ground Plane	NA	NA	Eating	NA	Sitting next to #39 and eating	40.721258	-73.950799
BROOKLYN	D	McCarren Park	22	D-22-39	Gray	Cinnamon, White	NA	Ground Plane	NA	NA	Eating	NA	Sitting next to #38 and eating	40.721217	-73.95077
BROOKLYN	D	McCarren Park	22	D-22-40	Cinnamon	White	NA	Ground Plane	NA	NA	Foraging	Indifferent	Fluffy	40.721173	-73.950781
BROOKLYN	D	McCarren Park	22	D-22-41	Cinnamon	Cinnamon	NA	Above Ground	NA	NA	Running, Foraging	Indifferent	Skinny	40.721161	-73.950732
BROOKLYN	D	McCarren Park	22	D-22-42	Gray	Gray	NA	Above Ground	NA	NA	Climbing	Indifferent	Clinging to tree	40.721124	-73.950797
BROOKLYN	D	McCarren Park	22	D-22-43	Gray	White	NA	Above Ground	10	NA	Running, Chasing, ClimbingIndifferent	Playing with another squirrel in a tree	40.721026	-73.950765
BROOKLYN	D	McCarren Park	22	D-22-44	Gray	Cinnamon, White	NA	Ground Plane	NA	NA	Foraging	Runs From	Ran very quickly	40.719376	-73.952326
```

This is very useful, but as you can see, this file is maybe a little big for this.  Often, to get a feel for a file like this one, it's useful to check out the first and last few lines of a file.  For this, we can use `head` and `tail`:

```bash
brooklyn $ head -3 mccarren_park_squirrels.txt
Area.Name	Area.ID	Park.Name	Park.ID	Squirrel.ID	Primary.Fur.Color	Highlights.in.Fur.Color	Color.Notes	Location	Above.Ground..Height.in.Feet.	Specific.Location	Activities	Interactions.with.Humans	Other.Notes.or.Observations	Squirrel.Latitude..DD.DDDDDD.	Squirrel.Longitude...DD.DDDDDD.
BROOKLYN	D	McCarren Park	22	D-22-01	Cinnamon	White	NA	Ground Plane	NA	NA	Eating	Indifferent	NA	40.72167	-73.953364
BROOKLYN	D	McCarren Park	22	D-22-02	Gray	White	NA	Ground Plane	NA	NA	Eating	Approaches	NA40.721768	-73.953192
brooklyn $ tail -3 mccarren_park_squirrels.txt
BROOKLYN	D	McCarren Park	22	D-22-42	Gray	Gray	NA	Above Ground	NA	NA	Climbing	Indifferent	Clinging to tree	40.721124	-73.950797
BROOKLYN	D	McCarren Park	22	D-22-43	Gray	White	NA	Above Ground	10	NA	Running, Chasing, ClimbingIndifferent	Playing with another squirrel in a tree	40.721026	-73.950765
BROOKLYN	D	McCarren Park	22	D-22-44	Gray	Cinnamon, White	NA	Ground Plane	NA	NA	Foraging	Runs From	Ran very quickly	40.719376	-73.952326
```

By default, `head` will return the first five lines of a file and `tail` will return the last five, but you can change this with a flag like above.  In the case of this park file, the first few lines are especially useful for telling us what kind of information is present in the file.

## Moving Files and Directories

There is a lot on our screen right now, so let's `clear` it.  You may have noticed by now that there is a file out of place:

```bash
bash_bootcamp $ ls squirrel_data
brooklyn			city_hall_park_squirrels.txt	upper_manhattan
central_manhattan		lower_manhattan
```

`city_hall_park_squirrels.txt` is currently not in an area directory.  Should it be?  View the file to figure out which area it belongs to.

If your answer is Lower Manhattan, you're correct!  But how do we move it there using the command line?

To move a file or directory, we can use `mv`.  To use `mv`, all we need to do is include the name of the thing we want to move (with a path if it's in another directory) and the name of the place we want to move it.

```bash
bash_bootcamp $ mv squirrel_data/city_hall_park_squirrels.txt squirrel_data/lower_manhattan
bash_bootcamp $ ls squirrel_data
brooklyn		central_manhattan	lower_manhattan		upper_manhattan
bash_bootcamp $ ls squirrel_data/lower_manhattan
battery_park_squirrels.txt		columbus_park.txt		teardrop_park_squirrels.txt
city_hall_park_squirrels.txt		corlears_hook_park_squirrels.txt
columbus_park.txt			seward_park_squirrels.txt
```

Now, `city_hall_park_squirrels.txt` is right where it belongs with the rest of the Lower Manhattan parks.

While we're here, I've noticed that one of the files has a different naming scheme than the others.  It's possible that `columbus_park.txt` should be `columbus_park_squirrels.txt`.  Let's take a look and see:

```bash
bash_bootcamp $ cd squirrel_data/lower_manhattan
lower_manhattan $ head -3 columbus_park.txt
Area.Name	Area.ID	Park.Name	Park.ID	Squirrel.ID	Primary.Fur.Color	Highlights.in.Fur.Color	Color.Notes	Location	Above.Ground..Height.in.Feet.	Specific.Location	Activities	Interactions.with.Humans	Other.Notes.or.Observations	Squirrel.Latitude..DD.DDDDDD.	Squirrel.Longitude...DD.DDDDDD.
327	LOWER MANHATTAN	C	Columbus Park	16	C-16-01	Gray	Cinnamon	Cinnamon streak down back	Ground Plane		Climbing, Eating, Foraging	Approaches	Boy, Alert ��� lots of basketball close by	40.714867	-74.000236
328	LOWER MANHATTAN	C	Columbus Park	16	C-16-02	Gray	Cinnamon		Ground Plane			Running, Foraging			40.7159	-74.000167
```

Yep, it looks like `columbus_park.txt` contains squirrel data just like the other files.  We should rename it so we don't get confused again.  It turns out that `mv` works for this as well.  All you need to do is provide the current name of the file and then the new name:

```bash
lower_manhattan $ mv columbus_park.txt columbus_park_squirrels.txt
lower_manhattan $ ls
battery_park_squirrels.txt		columbus_park_squirrels.txt		seward_park_squirrels.txt
city_hall_park_squirrels.txt		corlears_hook_park_squirrels.txt	teardrop_park_squirrels.txt
```

And, problem solved!  Before moving on, I'll also note that `mv` works exactly the same way for directories:

```bash
lower_manhattan $ cd ..
squirrel_data $ mv lower_manhattan brooklyn
squirrel_data $ ls
brooklyn		central_manhattan	upper_manhattan
squirrel_data $ mv brooklyn/lower_manhattan .
squirrel_data $
```

There is no need to run the above code, because the directories are all named correctly and in their proper place.  But, you should take note of the `.` and remember that it represents the current directory.

## Copying and Removing Files and Directories

If you ever need a file or directory to be present in more than one place, then you'll need the `cp` command.  Our files and directories are actually setup well for now, so I'll just demonstrate these commands for you.  No need to mess up your perfectly good data structure!

Copying files and directories with `cp` has the same syntax as `mv`.  The big difference is that the original file or directory will remain:

```bash
bash_bootcamp $ pwd
/Users/ameliaharrison/Desktop/bash_bootcamp
bash_bootcamp $ ls park_data
park_info.txt
bash_bootcamp $ cp park_data/park_info.txt squirrel_data
bash_bootcamp $ ls squirrel_data
brooklyn		central_manhattan	lower_manhattan		park_info.txt		upper_manhattan
bash_bootcamp $ ls park_data
park_info.txt
```

While in the `bash_bootcamp` directory, I've copied the file `park_info.txt` from the directory `park_data` to the directory `squirrel_data`.  Notice that the file now exists in two places.

But, I do not need this file in two places, so I want to delete it from `squirrel_data`.  I can do this with `rm` (remove):

```bash
bash_bootcamp $ rm squirrel_data/park_info.txt
bash_bootcamp $ ls squirrel_data
brooklyn		central_manhattan	lower_manhattan		upper_manhattan
bash_bootcamp $
```

Beware the `rm` command, for it shows no mercy.  The `rm` command does not move things to the trash, it simply deletes them forever, so you need to be careful with it.  If you want it to prompt you to confirm that you want to delete something, you can use the `-i` flag (check `man rm` for details).

Copying and removing can also be done with directories, but unlike move you will need a flag.  Again, you don't need to run these commands as I will demonstrate them for you.

```bash
bash_bootcamp $ cp -R park_data squirrel_data
bash_bootcamp $ ls
park_data	squirrel_data
bash_bootcamp $ ls squirrel_data
brooklyn		central_manhattan	lower_manhattan		park_data		upper_manhattan
bash_bootcamp $ rm -r squirrel_data/park_data
bash_bootcamp $ ls squirrel_data
brooklyn		central_manhattan	lower_manhattan		upper_manhattan
bash_bootcamp $ ls
park_data	squirrel_data
```

In this example, I copied the entire `park_data` directory into the `squirrel_data` directory.  Then, I removed it from `squirrel_data`.  Notice that the flag for `cp` is `-R` (uppercase) while for `mv` the flag is `-r` (lowercase).  Both are referring a concept called "recursion" which is what allows us to copy a directory and its contents.  We won't be talking about recursion outside of this capacity, but you can [read up on it](https://en.wikipedia.org/wiki/Recursion_(computer_science)) if you would like.

**BREAK**

## This is Where the Fun Begins

With all of that boring stuff out of the way, we can really start working with the files.  The commands and information before this section are sort of like utilities; they are very useful and we couldn't do anything else without them.  But, we're about to get into some of the really important commands and concepts for practical data analysis, which is much more fun.

### Working with Data in Files

For the next section, we will be working with the `tompkins_square_park_squirrels.txt` file.  It's in `squirrel_data/central_manhattan`, so let's head there now.  I have been hanging out in `bash_bootcamp`, but there is a good chance you are in another directory so you will have to figure out how to get to `central_manhattan`.

```bash
bash_bootcamp $ cd squirrel_data/central_manhattan
central_manhattan $ ls
lindsay_east_river_park_squirrels.txt	stuyvesant_square_park_squirrels.txt	union_square_park_squirrels.txt
madison_square_park_squirrels.txt	tompkins_square_park_squirrels.txt	washington_square_park_squirrels.txt
central_manhattan $
```

Let's check out `tompkins_square_park_squirrels.txt` a little while we're here.  Try to print the first four and last two lines to the screen.

Alright, so this file looks just like the others (except for some of the data).  That means that whatever we do this file will be applicable to all of the files, which will be important later.  For now, we are going to try to answer a few questions about the squirrels in [Tompkins Square Park](https://www.nycgovparks.org/parks/tompkins-square-park).

1. How many squirrels were counted in Tompkins Square Park?
2. What activities were the squirrels doing?
3. What primary colors were the squirrels?
4. How many squirrels of each primary color were observed?

These are all questions that you might want to know the answer to as a squirrel researcher.  You could open up the table in a spreadsheet application and answer them there (and if you have small files, that's usually easier than firing up the command line), but you can also answer them right here and now.

As I'm sure you could have predicted, we'll start with **Question 1: How many squirrels were counted in Tompkins Square Park?**

Before answering this question, let's think about the format of the file.  `tompkins_square_park_squirrels.txt` and all of the other text files are tab-separated or tab-delimited files.  This means that they are tables that are separated by tab characters.  The most common file extensions for these files are `.txt`, `.tsv`, and `.btab`.  

Now, I know for sure that these files are tab-separated because I made them.  You could probably guess that they are tab-separated by viewing the files with `less` because of all of the empty spaces between columns.  But for you to be sure, you can run the command `od -c`:

```bash
central_manhattan $ od -c tompkins_square_park_squirrels.txt
0000000    A   r   e   a   .   N   a   m   e  \t   A   r   e   a   .   I
0000020    D  \t   P   a   r   k   .   N   a   m   e  \t   P   a   r   k
0000040    .   I   D  \t   S   q   u   i   r   r   e   l   .   I   D  \t
0000060    P   r   i   m   a   r   y   .   F   u   r   .   C   o   l   o
0000100    r  \t   H   i   g   h   l   i   g   h   t   s   .   i   n   .
0000120    F   u   r   .   C   o   l   o   r  \t   C   o   l   o   r   .
0000140    N   o   t   e   s  \t   L   o   c   a   t   i   o   n  \t   A
```

The output is pretty long, so I've only included the first few lines here.  What `od -c` does is print out each character in a file, including whitespace characters.  Whitespace characters are those which are invisible to you, but not to the computer.  Many formatting characters are whitespace.  The most common examples are tabs (`\t`), newlines (`\n`), and carriage returns (`\r`).  This is a very important concept to be aware of because often a file that looks perfectly good to your human eyes will cause your computer to throw a fit.  When this is the case, check the whitespace characters.

As you can see, there are a lot of `\t` (tab) characters in the above file between what we know to be column headers, which confirms that we are dealing with a tab-delimited table.  Awesome.  Now, use `less` to figure out what each of the rows represents.

You should have noticed that each row represents a squirrel.  So, maybe we can get the number of squirrels by counting the number of lines in the file?  We can do that with the word count command (`wc`):

```bash
central_manhattan $ wc -l tompkins_square_park_squirrels.txt
      60 tompkins_square_park_squirrels.txt
```

The word count command with the `-l` flag let's us count the number of lines in a file.  In this case, there are 60 lines. So, that means there are 60 squirrels!  Question answered!  Well. . .not quite.  There is an issue with this method, any idea what it is?

There is a line in the file that does not represent a squirrel: the header line with the names of the columns.  It turns out we counted this line along with the others.  So, we actually have 59 squirrels.

Now, you could stick with this method of counting lines and subtracting 1 to get the number of squirrels, but can we get the number of squirrels directly?  The answer is yes.  There are multiple ways to do this (as with many file manipulations on the command line), but I'll only show you one for now, using `grep`.

`grep` is my favorite command.  There are so many possibilities!  As legend has it, you can become all-powerful by knowing the ins and outs of `grep`, `sed`, and `awk`.  We will see limited uses of `grep` and `sed` today and no `awk`, but there are many resources out there on all three.

Okay, back to `grep`.  One of the fun things to do with `grep` is counting.  The problem with the line count was the header.  To count only the squirrel lines, we need to find something that is present in all other lines, but not in the header.  There are a few possible answers, but I went with the area name:

```bash
grep -c "CENTRAL MANHATTAN" tompkins_square_park_squirrels.txt
59
```

As you can see, this returns the correct answer of 59 squirrels.  One question down!

Predictably, we will now proceed to **Question2: What activities were the squirrels doing?**

Take a look at the table with `less` again.  You will notice that there is a column called `Activities`, which is where our information will come from.  Before moving forward, we need to think about what we want our result to be.  In the table, we can see that the activities are fairly standardized (only a few possible responses) and are repeated.  Ideally, we want to print out a list of unique (non-redundant) values in the `Activities` column.

Now that we have a goal, we can think about how to achieve it.  To start, we need to grab that `Activities` column.  We can use `cut` for this.  Take a look at the `cut` manual and try to figure out a strategy.

For our purposes, `cut -f` will be perfect, as we want to pull a field in each line of a tab-separated file (tabs are the default demilimiters for `cut`).  It's a little hard to figure out exactly what to do from the man page, so let's experiment.

```bash
central_manhattan $ cut -f tompkins_square_park_squirrels.txt
cut: [-bcf] list: illegal list value
```

Oooookay, so `cut -f` on its own does not work.  If we take a look down at the examples on the man page, we can see numbers in the command.  I wonder what those will do?

```bash
central_manhattan $ cut -f1 tompkins_square_park_squirrels.txt
Area.Name
CENTRAL MANHATTAN
CENTRAL MANHATTAN
....
```

Ah, so we've extracted the first column from the file.  Does that mean we just need to count the columns until we get to `Activities` and then put that number in?  Well, yes!

```bash
central_manhattan $ cut -f12 tompkins_square_park_squirrels.txt
Activities
Climbing
Foraging
....
```

Alright, so we've got the correct column.  How do we get unique values?  With `uniq`:

```bash
central_manhattan $ cut -f12 tompkins_square_park_squirrels.txt | uniq
Activities
Climbing
Foraging
Running
Foraging
....
```

Well the list is shorter, but not quite unique.  And hold up, what is that weird line?

This `|` is a pipe.  It's called a pipe because it allows the output of one command to flow to a new command.  In this case, we took the output from `cut`, which was our `Activities` column, and sent it to the `uniq` command.  Make sense?  It's a fairly simple concept, but a little jarring at first.

Now, as for why we still don't have unique values, the last line of the description on the man page reads: "Repeated lines in the input will not be detected if they are not adjacent, so it may be necessary to sort the files first."  Basically, we need to sort the column contents first to be in alphabetical order, which we can do with `sort`:

```bash
central_manhattan $ cut -f12 tompkins_square_park_squirrels.txt | sort | uniq
Activities
Chasing
Climbing
Climbing (down tree)
Climbing (down)
Foraging
Lounging
Running
Sitting
Sitting (in tree hole)
```

And there you have it, a unique list! You'll notice that some of the survey volunteers went into some extra detail and added to the standard responses, which has messed up the list a little.  We aren't going to worry about that right now, but this is why "data cleaning" is necessary before data analysis.  

Now that we have answered the second question we can move onto **Question 3: What primary colors were the squirrels?**

This question should be easy to answer now.  Just grab the `Primary.Fur.Color` column with `cut`, pipe the result through `sort`, and then pipe that result through `uniq`.  I will put the answer here, but not the code.  You should get the following list:

```bash
Black
Gray
Primary.Fur.Color
```

Looks like there are only Black and Gray squirrels in Tompkins Square Park.  Notice that `Primary.Fur.Color`, the column name, got all the way to the bottom.  It wasn't apparent in Question 2 because `Activities` came first in alphabetical order, but the column names are being treated the same as the column values.  Later, we will see a way to deal with this, but for now we will ignore it.

Finally, we have **Question 4: How many squirrels of each primary color were observed?**

We know that there are two colors of squirrel in this park, black and gray.  Now, we just need to know how many of each.  Take another look at the man page for `uniq`.  You should find that all you need to answer this question is to add the `-c` flag to the command that answered the last question:

```bash
central_manhattan $ cut -f6 tompkins_square_park_squirrels.txt | sort | uniq -c
   4 Black
  55 Gray
   1 Primary.Fur.Color
```

So our answer is, 4 black squirrels and 55 gray squirrels.  Notice that this adds up correctly to 59.  Adding in the `Primary.Fur.Color` gets us the correct number of file lines (60).

**BREAK**

### Combining files

Right now, all of the squirrel data is broken up by park, but we want to analyze all of the data together.  For that, we will need to create another file containing all of the information.  How can we do that?

Depending on what the files look like, this can be super easy or a little fiddly.  Remember the `cat` command from earlier?  So far, we have only used it to print files to the screen, but it's actually short for "concatenate," which means to link things together.  `cat` is the easiest way to combine files, so let's try that first.

The most logical place for a table containing data about all of the squirrels is probably `squirrel_data`, so let's head there now. 

```bash
central_manhattan $ cd ..
squirrel_data $
```

Now, let's remind ourselves of where all of the files are.  We want to list the contents of the current directory, but also all of the area directories.  We can do this with globs:

```bash
squirrel_data $ squirrel_data $ ls *
brooklyn:
mccarren_park_squirrels.txt		msgr_mcgolrick_park_squirrels.txt

central_manhattan:
lindsay_east_river_park_squirrels.txt	stuyvesant_square_park_squirrels.txt	union_square_park_squirrels.txt
madison_square_park_squirrels.txt	tompkins_square_park_squirrels.txt	washington_square_park_squirrels.txt

lower_manhattan:
battery_park_squirrels.txt		columbus_park_squirrels.txt		seward_park_squirrels.txt
city_hall_park_squirrels.txt		corlears_hook_park_squirrels.txt	teardrop_park_squirrels.txt

upper_manhattan:
fort_tryon_park_squirrels.txt		j_hood_wright_park_squirrels.txt	riverside_park_squirrels.txt
highbridge_park_squirrels.txt		marcus_garvey_park_squirrels.txt	st_nicholas_park_squirrels.txt
squirrel_data $
```

Globs (`*`) are "catch-all" characters that select everything.  In the command above (`ls *`), the glob character matched all of the contents of the directory, which are the four area directories, and asked for their contents to be listed.  The output even told us which directory holds which files.

Globs don't always have to isolated like this.  They can also be used to help match specific patterns.  For example, let's say we only wanted to see the contents of the Manhattan directories.  We could use this command instead:

```bash
squirrel_data $ ls *_manhattan
central_manhattan:
lindsay_east_river_park_squirrels.txt	stuyvesant_square_park_squirrels.txt	union_square_park_squirrels.txt
madison_square_park_squirrels.txt	tompkins_square_park_squirrels.txt	washington_square_park_squirrels.txt

lower_manhattan:
battery_park_squirrels.txt		columbus_park_squirrels.txt		seward_park_squirrels.txt
city_hall_park_squirrels.txt		corlears_hook_park_squirrels.txt	teardrop_park_squirrels.txt

upper_manhattan:
fort_tryon_park_squirrels.txt		j_hood_wright_park_squirrels.txt	riverside_park_squirrels.txt
highbridge_park_squirrels.txt		marcus_garvey_park_squirrels.txt	st_nicholas_park_squirrels.txt
```

This time, the `brooklyn` directory isn't listed because it doesn't contain the string `_manhattan`.  `*_manhattan` will only match with names that contain `_manhattan`.  A file or directory name could have anything before `_manhattan` and match, but it must contain `_manhattan`.  You can also put globs at the end or in the middle:

```bash
ls *_man*
central_manhattan:
lindsay_east_river_park_squirrels.txt	stuyvesant_square_park_squirrels.txt	union_square_park_squirrels.txt
madison_square_park_squirrels.txt	tompkins_square_park_squirrels.txt	washington_square_park_squirrels.txt

lower_manhattan:
battery_park_squirrels.txt		columbus_park_squirrels.txt		seward_park_squirrels.txt
city_hall_park_squirrels.txt		corlears_hook_park_squirrels.txt	teardrop_park_squirrels.txt

upper_manhattan:
fort_tryon_park_squirrels.txt		j_hood_wright_park_squirrels.txt	riverside_park_squirrels.txt
highbridge_park_squirrels.txt		marcus_garvey_park_squirrels.txt	st_nicholas_park_squirrels.txt

squirrel_data $ ls *_*hat*
central_manhattan:
lindsay_east_river_park_squirrels.txt	stuyvesant_square_park_squirrels.txt	union_square_park_squirrels.txt
madison_square_park_squirrels.txt	tompkins_square_park_squirrels.txt	washington_square_park_squirrels.txt

lower_manhattan:
battery_park_squirrels.txt		columbus_park_squirrels.txt		seward_park_squirrels.txt
city_hall_park_squirrels.txt		corlears_hook_park_squirrels.txt	teardrop_park_squirrels.txt

upper_manhattan:
fort_tryon_park_squirrels.txt		j_hood_wright_park_squirrels.txt	riverside_park_squirrels.txt
highbridge_park_squirrels.txt		marcus_garvey_park_squirrels.txt	st_nicholas_park_squirrels.txt
```

Now that we have seen a couple of glob examples, let's think about how we can use them to help us make our file.  Before the glob tangent, we were talking about `cat`.  The syntax for using `cat` is 

```bash
cat file1 file2 file3
```

You can put however many files you want, and cat will chain them together.  As it is now, though, the result will print to the screen, and we want a file.  To put the output into a new file, we can use a different kind of pipe:

```bash
cat file1 file2 file3 > new_file
```

The above command will now string the contents of files 1, 2, and 3 together and put them into a new file.  When sticking things into files, the pipes to use are `>` and `>>`.  The single `>` will overwrite an existing file of the same name, while the double `>>` will add to the end.  We will see this in action later.

Okay, so if `cat` sticks files together, globs select multiple files at once, and `>` pipes things to new files, what are we waiting for?  Time to make our master file.

```bash
squirrel_data $ cat */*_park_squirrels.txt > all_park_squirrels.txt
```

Try to describe what this command is doing.  It's selecting every file that ends in `_park_squirrels.txt` from every directory, stringing them together, and sending that to a new file in the current directory called `all_park_squirrels.txt`.  If you type `ls`, you should see your new file!  Use `less` to check it out.

Unfortunately, we have an issue.  You may have noticed that because every file has a header row with column names, we now have 20 of those rows sprinkled throughout our new file.  

There are a couple of options for fixing this.  We could remove all of the header rows, but this could be tricky because we do want to keep one.  Alternatively, we could sort the file based on the first column of the header (`Area.Name`) and then remove the first 20 rows.  That row should be first alphabetically.  Lastly, we could build the file again in a way that keeps us from having this problem in the first place.

The last two options are viable, so I'll show you how to do both.  First, let's try sorting the file and deleting the first few lines.  If you go to the `sort` man page, you will see that we can specify columns to sort on, similar to `cut`.  To sort on the first column, we would use `sort -k 1`.  Now, we want to figure out if we can edit the file "in place," i.e., can we edit the file and have the changes stick or do we have to make a new file to put the sorted data into?  It turns out we can edit it in place by specifying the current file as the output with `-o`:

```bash
squirrel_data $ wc -l all_park_squirrels.txt
     453 all_park_squirrels.txt
squirrel_data $ sort -k 1 all_park_squirrels.txt -o all_park_squirrels.txt
squirrel_data $ head -3 all_park_squirrels.txt
Area.Name	Area.ID	Park.Name	Park.ID	Squirrel.ID	Primary.Fur.Color	Highlights.in.Fur.Color	Color.Notes	Location	Above.Ground..Height.in.Feet.	Specific.Location	Activities	Interactions.with.Humans	Other.Notes.or.Observations	Squirrel.Latitude..DD.DDDDDD.	Squirrel.Longitude...DD.DDDDDD.
Area.Name	Area.ID	Park.Name	Park.ID	Squirrel.ID	Primary.Fur.Color	Highlights.in.Fur.Color	Color.Notes	Location	Above.Ground..Height.in.Feet.	Specific.Location	Activities	Interactions.with.Humans	Other.Notes.or.Observations	Squirrel.Latitude..DD.DDDDDD.	Squirrel.Longitude...DD.DDDDDD.
Area.Name	Area.ID	Park.Name	Park.ID	Squirrel.ID	Primary.Fur.Color	Highlights.in.Fur.Color	Color.Notes	Location	Above.Ground..Height.in.Feet.	Specific.Location	Activities	Interactions.with.Humans	Other.Notes.or.Observations	Squirrel.Latitude..DD.DDDDDD.	Squirrel.Longitude...DD.DDDDDD.
squirrel_data $ wc -l all_park_squirrels.txt
     453 all_park_squirrels.txt
```

As you can see, we now have a file with all of the headers at the top.  Now, we just have to remove the first 19 rows.  We will keep row 20 so that we still have column names. 

There are lots of ways to remove a specified number of rows, including with `tail`, `awk`, and `sed`.  I will show you `sed` because it will also be part of our other solution.  

`sed` is another magical command.  It's a stream editor, which means that it is designed to modify text files without reading them completely into memory.  This is especially important when you have very large files.  There is a lot to `sed`; you could probably teach a whole course with just `sed`, `awk`, and `grep`, so this is small potatoes.  

Looking at the man page, we can see that `sed` allows us to edit a file in place using `-i`, so we will need that.  I will spare you from having to go through the rest of the documentation because it's very long and just show you the final command:

```bash
squirrel_data $ sed -i 1,19d all_park_squirrels.txt
```

If you are on a Mac, use this command [instead](https://stackoverflow.com/questions/4247068/sed-command-with-i-option-failing-on-mac-but-works-on-linux/14813278#14813278):

```bash
squirrel_data $ sed -i'.bak' 1,19d all_park_squirrels.txt
```

Both commands say to take the `all_park_squirrels.txt` file and remove lines 1 through 19.  If you use head to show the first two rows you will see that we are down to the only one header row.  Huzzah!

Now, I did say that I would show you how to avoid this problem in the first place, but you will have to wait for the next lesson.  For now, we will move on.

### Comparing files

A lot of what you do in data analysis is comparison.  It's also a common way to check that you haven't accidentally deleted or lost any data in your command line journey.  I promise we haven't lost any data this time, so we are just going to try to answer a question: Were squirrels observed in all New York City Parks?

To answer this question, we will need the `all_park_squirrels.txt` file we just created and the `parks_info.txt` file.  Let's move up a directory to start so that we are the same distance away from both files.

```bash
squirrel_data $ cd ..
bash_bootcamp $
```

We are pretty familiar with the squirrel file, so let's remind ourselves of what the park file looks like:

```bash
bash_bootcamp $ head -3 park_data/park_info.txt
Area.Name	Area.ID	Park.Name	Park.ID	Date	Start.Time	End.Time	Total.Time..in.minutes..if.available.	Park.Conditions	Other.Animal.Sightings	Litter	Temperature...Weather	Number.of.Squirrels	Squirrel.Sighter.s.	Number.of.Sighters
UPPER MANHATTAN	A	Fort Tryon Park	1	3/1/20	3:14:00 PM	4:05:00 PM	51	Busy	Humans, Dogs, Pigeons, Cardinals	Some	43 degrees, sunny	12	01, 02, 03, 04	4
UPPER MANHATTAN	A	J. Hood Wright Park	2	3/1/20	3:30:00 PM	4:00:00 PM	30	Calm	Humans, Hawks, Dogs, Pigeons, Rat	Some, in trees	cold, clear	24	05, 06	2
bash_bootcamp $ wc -l park_data/park_info.txt
      26 park_data/park_info.txt
```

Judging form the line count, it looks like there are more parks in `park_info.txt` than in `all_park_squirrels.txt` (remember there were only 20 files to combine).  Let's say, as squirrel researchers, we really want to know in which parks there were no squirrels observed.  The best way to answer this is with `comm`.

The `comm` command can be used to compare two lists.  By default, it returns three lists: lines only in file1; lines only in file2; and lines in both files.  The man page is short and clear, but also confusing.  It always takes me awhile to remember which flags to use.  That is because, unlike most commands, the `comm` flags indicate which columns to *suppress*, rather than which columns or services to provide.

So we can use `comm` to compare lists, but we don't currently have any lists.  We need a list of all parks in the park data and the squirrel data.  Luckily, we know how to do that!  A quick note before we do, the `comm` man page warns us that the files "should be sorted lexically," so we should be sure to use `sort` somewhere in this process.

For `park_info.txt`, each park only appears once, so we only need to grab the correct column, sort it, and send the output to a new file:

```bash
bash_bootcamp $ cut -f3 park_data/park_info.txt | sort > all_parks_list.txt
```

For `all_park_squirrels.txt`, the parks do repeat, so we need to make sure to also use `uniq`.

```bash
bash_bootcamp $ cut -f3 squirrel_data/all_park_squirrels.txt | sort | uniq > parks_with_squirrels.txt
```

Look at all those pipe!  It's beautiful!

Now, all that's left is the comparison.  If we want to know in which parks there were 0 squirrel observations, we can use this command:

```
bash_bootcamp $ comm -23 all_parks_list.txt parks_with_squirrels.txt
Cooper Park
Riverside Park (section near Grant Memorial)
Sara D. Roosevelt Park (Section Above Delancey St)
Sara D. Roosevelt Park (Section Below Delancey St)
Sternberg Park
Thomas Paine Park
```

There are six parks with 0 squirrel observations.  My guess is that there were no volunteers covering those parks for this survey.  But wait, there were 25 parks in `parks_info.txt` and 20 in `all_park_squirrels.txt`.  There should only be five parks with 0 squirrel sightings.  Try suppressing the first column instead of the second.  This will give us parks in `all_park_squirrels.txt` that are not in `parks_info.txt`.

```bash
comm -13 all_parks_list.txt parks_with_squirrels.txt
Riverside Park (Section Near Grant Memorial)
```

Ah, I see the problem.  In the parks data, "section" is not capitalized, but it is in the squirrel data.  Another reason why data cleaning is so important!

# Conclusions

In this lesson, you learned a lot of ways to play around with text files including moving and deleting them, editing them, and creating new files.

Next, we're going to build the big squirrel dataset again.  But this time, with a script!