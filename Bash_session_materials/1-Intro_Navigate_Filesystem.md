*Before beginning the lesson, please download the zipped directory `squirrel_census.zip` from the bootcamp GitHub page.  Unzip the file and place it on your Desktop.*

# Introduction to Bash

Bash is a Unix shell and command language.  There are other shells out there, but bash is the most ubiquitous.  But what is a shell, anyway?

## Shells and Kernels

At the core of every computer operating system, is a kernel.  The kernel interfaces directly with the hardware and essentially acts as the bridge between you and your computer.  But, we also need a path to get to this bridge, and that is a shell.  

A shell is an interface between you and the kernel that allows you to access the operating system.  We can use shells to execute programs and commands.

## Using shells

To utlize shells, we need a command line application, also commonly called a terminal.  The basis of any such program is a shell of one kind or another.  There, you can type commands and execute them with `enter` or `return`.  You should have downloaded or made sure you could open a terminal during the setup.  Go ahead and open those up now.

## What makes bash special?

Bash stands for Bourne-Again SHell, which is a play on an older shell called the Bourne shell.  The Bourne shell was developed in the late 1970s by Stephen Bourne at Bell Labs (later AT&T).  For a long time, it was the default shell of Unix, which is the OS for Macs.  Unix and the Bourne shell were awesome, but they were also closed source and paid.  In response, programmers wanting free and open source counterparts created Bash and Linux, and the rest is history!  This also is why you didn't need to install extra programs for this session if you have a Mac or Linux machine.

# Navigating the file system

One of the most common things you will do in bash is move around your file system.  By file system, we are referring to the composite of your folders, files, applications, etc.

You should have installed or tried to open a terminal during the setup.  Go ahead and open up that program now.  Windows users, make sure that you are running a Bash shell.

You should see something fairly similar to this, though the exact appearance of your command line prompt will depend on the exact program and any settings you may have changed.  

```bash
Last login: Fri May 27 15:28:53 on ttys003
~ $ 
```

The `$` you see above is the command prompt.  This is where you will type any commands.  You will execute them using the `enter` or `return` key depending on your keyboard layout.

## The Home Directory

When you first open your terminal, you start at the very top of your file system.  This means that you are essentially sitting above everything on your computer, including Documents, Downloads, Applications, etc.  This is your **home directory** and it is represented by `~`.  The location of your home directory is also stored as the variable `$HOME`.  To get the location of your home variable, type:

```bash
Last login: Fri May 27 15:28:53 on ttys003
~ $ echo $HOME
```

and hit `enter`.  The resulting string of characters is your home directory.  Mine is `/Users/ameliaharrison`.

## Some Vocabulary

Let's take a quick moment to talk about vocabulary.  When navigating through the file system, there are generally two types of things you will be dealing with: directories and files.

* **Files** are exactly what you think they are - an object that stores information of some kind.

* **Directories** are almost exactly like folders, in that they contain a collection of files and sometimes other directories.  The difference between a folder and a directory is that a directory is mapped to a physical location on your harddrive, whereas folders don't need to be and are a more abstract concept to the computer.  This distinction doesn't matter most of the time, but it's the reason why we refer to directories when using the command line and folders when using a GUI.

* **Paths** describe the location of something on your computer and are therefore very important for navigation.  When working at the command line, you will often need to provide the location of a file or directory.  Paths can be either absolute or relative.

	*   **Absolute paths** provide the location of a file or directory with respect to the home directory.  Therefore, they always start from `~`, `$HOME`, or the actual path to your home directory (in my case, `/Users/ameliaharrison`).
	*   **Relative paths** provide the location of a file or directory with respect to the directory that you are currently in.  When you are still in the home directory as we are now, the relative and absolute paths to a file or directory are the same.  However, once you change the directory, the relative path to another file or directory also changes.
	*   *Tip:* If you ever need to know the path to your current directory, you can execute the command `pwd`, which stands for Print Working Directory.

* **Standard Out** is where many commands print their output.  If output is printed directly to the screen, they are printing to standard out.
	
We will be using these terms and looking at examples along the way, so don't worry if you're not sure you understand them yet.

## Listing Directories

*If you have not already done so, now is a good time to download the zipped directory `squirrel_census.zip` from the bootcamp GitHub page.  Then, unzip the file and place it on your Desktop.*

Before we can think about moving from the home directory, we have to know where we can go.  The first step of figuring that out is to list the contents of the home directory.  To do this, you will type `ls` into the command prompt and hit `enter`.

```bash
~ $ ls
Applications			Music
CytoscapeConfiguration		Pictures
Desktop				Public
Documents			Virtual Machines.localized
Downloads			VirtualBox VMs
Dropbox				cv_webpage
Geneious 10.2 Data		geneious-nexus
Geneious 2021.2 Data		igv
Geneious 2022.0 Data		miniconda3
Library				projects
Movies				software
```

As you can see, the `ls` command lists the contents of my home directory in alphabetical order.  For a more thorough look at the contents, we can use `ls -l`.  

```bash
~ $ ls -l
total 0
drwx------@  5 ameliaharrison  staff   160 Sep  8  2021 Applications
drwxr-xr-x  27 ameliaharrison  staff   864 Sep 17  2021 CytoscapeConfiguration
drwx------@  7 ameliaharrison  staff   224 May 25 18:43 Desktop
drwx------@ 37 ameliaharrison  staff  1184 May 27 18:39 Documents
drwx------@ 16 ameliaharrison  staff   512 May 27 12:49 Downloads
drwx------@ 19 ameliaharrison  staff   608 Nov 29 14:43 Dropbox
drwxr-xr-x  25 ameliaharrison  staff   800 Aug 22  2021 Geneious 10.2 Data
drwxr-xr-x  27 ameliaharrison  staff   864 Nov 30 12:40 Geneious 2021.2 Data
drwxr-xr-x  27 ameliaharrison  staff   864 Apr 27 23:11 Geneious 2022.0 Data
drwx------@ 95 ameliaharrison  staff  3040 May  6 19:24 Library
drwx------+  9 ameliaharrison  staff   288 Dec  6 10:12 Movies
drwx------+  4 ameliaharrison  staff   128 Oct 20  2020 Music
drwx------+  5 ameliaharrison  staff   160 Oct 20  2020 Pictures
drwxr-xr-x+  4 ameliaharrison  staff   128 Oct 19  2020 Public
drwxr-xr-x   5 ameliaharrison  staff   160 Mar 18 16:19 Virtual Machines.localized
drwx------   3 ameliaharrison  staff    96 Feb  3 15:46 VirtualBox VMs
drwxr-xr-x   5 ameliaharrison  staff   160 Dec  1  2020 cv_webpage
drwxr-xr-x  12 ameliaharrison  staff   384 Jan  5  2021 geneious-nexus
drwxr-xr-x   5 ameliaharrison  staff   160 Nov  5  2021 igv
drwxr-xr-x  15 ameliaharrison  staff   480 Feb  2 20:53 miniconda3
drwxr-xr-x   5 ameliaharrison  staff   160 Feb 12 22:10 projects
drwxr-xr-x  17 ameliaharrison  staff   544 Feb 23 20:15 software
```

Here, `-l` is a **flag** which is essentially an argument taken by the **command** `ls` that provides us with a different output than the command alone.  

The output of `ls -l` is a little harder to interpret than just `ls`.  How do we find out what all of these fields mean?

## Getting Help

The internet is a great source for solutions and almost anything you need to do on the command line is a short search away (if you know the right terms to use), but you don't always need to leave the command line for assistance.

Back to our `ls` example. We want to know more about `ls -l` and what information is included in the output.  To find out, let's manke a new tab and execute this command:

```bash
~ $ man ls
```

This brings us to the manual (man) page for the `ls` command.  Scrolling down through the flags, we can see that using `-l` has this impact:

```bash
-l      (The lowercase letter “ell”.) List files in the long format, as described in the The Long Format subsection below.
```

The man page gives a very good description of the long format.  As you have access, I won't copy all of the info here except for this: 

```bash
The following information is displayed for each file: file mode, number of links, owner name, group name, number of bytes in the file, abbreviated month, day-of-month file was last modified, hour file last modified, minute file last modified, and the pathname.
```

To leave the man page, hit `q` and then `enter` and you will be returned to the screen with your output.

## Clearing your screen

If you are ever feeling overwhelmed by everything on your screen, you can use the `clear` command.  Try executing it now.

After running `clear` you should get a screen that is blank except for a prompt at the very top.  If you're worried about losing past outputs and commands, don't!  Scrolling up will show you that everything is still there, just moved out of sight.

## Changing Directories

We know a bit about looking around now, but what about moving around?

To move within the file system we need to change directories, which is done with the `cd` command.  Let's move into the directory `bash_bootcamp` that was provided to you.  If you have not unzipped the file, you need to do so now.

First, let's make sure that the directory is on the desktop.  We can use `ls` and paths for this.

```bash
~ $ ls Desktop/
bash_bootcamp
```

Looks like it's right where it needs to be, so let's move in.

```bash
~ $ cd Desktop/bash_bootcamp
bash_bootcamp $
```

There will be output printed to the screen, but you should see the name of the current directory and likely the path to it to the left of the `$`.

A quick note, if you type `cd` and nothing after it, you will be taken to the home directory:

```bash
bash_bootcamp $ cd
~ $ 
```

To get back to `bash_bootcamp`, you can either type the command out again or use the up arrow on your computer to go back through past commands.  Hitting up twice should get you back to this command:

```bash
~ $ cd Desktop/bash_bootcamp
bash_bootcamp $
```

## Exploring

Now that we know a bit about looking and moving, let's kick it up a notch and really explore this directory.  If you run `ls` from the `bash_bootcamp` directory, you should see two more directories:

```bash
bash_bootcamp $ ls
park_data	squirrel_data
bash_bootcamp $
```

Let's take a look at the `park_data` directory first.  Move into the `park_data` directory and list the contents.  You should find that the directory contains a single text file called `park_info.txt`. 

We'll do a lot of work with files in a bit, but for now let's keep exploring.  First, we'll move back to the main `bash_bootcamp` directory.  Last time we moved backwards, we went all the way back to the home directory and then moved forward again.  But, you can jump back one back at a time with `..`

```bash
park_data $ cd ..
bash_bootcamp $
```

Now that we're back in `bash_bootcamp`, let's take a look at the directory `squirrel_data`.  We could keep using `ls`, but another really useful command for surveying directories and their contents is `tree`:

```bash
bash_bootcamp $ tree
.
├── park_data
│   └── park_info.txt
└── squirrel_data
    ├── brooklyn
    │   ├── mccarren_park_squirrels.txt
    │   └── msgr_mcgolrick_park_squirrels.txt
    ├── central_manhattan
    │   ├── lindsay_east_river_park_squirrels.txt
    │   ├── madison_square_park_squirrels.txt
    │   ├── stuyvesant_square_park_squirrels.txt
    │   ├── tompkins_square_park_squirrels.txt
    │   ├── union_square_park_squirrels.txt
    │   └── washington_square_park_squirrels.txt
    ├── city_hall_park_squirrels.txt
    ├── lower_manhattan
    │   ├── battery_park_squirrels.txt
    │   ├── columbus_park.txt
    │   ├── corlears_hook_park_squirrels.txt
    │   ├── seward_park_squirrels.txt
    │   └── teardrop_park_squirrels.txt
    └── upper_manhattan
        ├── fort_tryon_park_squirrels.txt
        ├── highbridge_park_squirrels.txt
        ├── j_hood_wright_park_squirrels.txt
        ├── marcus_garvey_park_squirrels.txt
        ├── riverside_park_squirrels.txt
        └── st_nicholas_park_squirrels.txt

6 directories, 21 files
```

Here, we can see the structure of `bash_bootcamp`, which is represented by the `.` at the top.  As we discovered earlier, `park_data` contains a single text file called `park_info.txt`.  `squirrel_data`, on the other hand is much larger.  It contains four directories, each labeled with a region in New York City.  Within each of those folders is a collection of text files that look to contain data on squirrels from 20 parks.

# Conclusions

In this lesson, you learned some of the history of bash, a decent amount of vocabulary, and how to navigate the file system.  

In the next lesson, we'll poke around those text files and see what we can do with them.

