# All commands for Bash session

## 1. Intro to Bash and Navigating the File System

```bash
echo $HOME

ls

ls -l
```

Talk about getting help

```bash
man ls

grep --help

clear
```

Move to the downloaded directory and poke around

```bash
cd Desktop/bash_bootcamp

cd

cd Desktop/bash_bootcamp

ls

ls park_data

ls squirrel_data

ls squirrel_data/upper_manhattan

tree

tree .
```

View a couple of files

```bash
less park_data/park_info.txt  # q to quit

cd squirrel_data/brooklyn

ls -l

less mccarren_park_squirrels.txt
```

Show how to get file paths

```bash
cd squirrel_data/upper_manhattan

pwd

ls

pwd riverside_park_squirrels.txt

realpath riverside_park_squirrels.txt
```

Moving, copying, and viewing files

City hall park isn't in a directory.  How to move it into the right one?

```bash
# figure out which group it belongs to
cd ..

ls

head city_hall_park_squirrels.txt

# it belongs to lower manhattan
mv city_hall_park_squirrels.txt lower_manhattan/

ls lower_manhattan/

# can also use mv to change file and directory names
head columbus_park.txt

mv lower_manhattan columbus_park.txt lower_manhattan columbus_park_squirrels.txt # make sure to spell squirrels right

# can also copy files
cd ..

ls

ls park_data

cp park_data/park_info.txt squirrel_data/

ls squirrel_data

ls park_data

# and you can copy directories
cp -R park_data/ squirrel_data/

ls

ls park_data

ls squirrel_data

# copying all directory contents
mkdir brooklyn_squirrel_data

cp squirrel_data/brooklyn/* brooklyn_squirrel_data
```

Removing things

```bash
# declutter the squirrel_data directory
cd squirrel_data

ls

rm park_info.txt

rm -r park_data

# get students to tell you how to do this
cd ..

rm -r brooklyn_squirrel_data
```

**BREAK**

## 2. Working with Text Files

Pick one of the park zones

```bash
ls squirrel_data/*
```

Tompkins Square Park

```bash
cd squirrel_data/central_manhattan

# open the file
less tompkins_square_park_squirrels.txt

# print the file to the screen
cat tompkins_square_park_squirrels.txt # prints to standard output**

# print the beginning and end of the table
head tompkins_square_park_squirrels.txt

tail tompkins_square_park_squirrels.txt

# print only the first and last lines
head -1 tompkins_square_park_squirrels.txt

tail -1 tompkins_square_park_squirrels.txt

# How many squirrels were counted in madison square park?
# count the lines
wc -l tompkins_square_park_squirrels.txt

# count the central manhattan (something that's in every line)
grep -c "CENTRAL MANHATTAN" tompkins_square_park_squirrels.txt

# What color squirrels are there in the park?
# Need to look at the primary fur color column
man cut # have students try to figure out what to do

cut -f1 tompkins_square_park_squirrels.txt

cut -f2 tompkins_square_park_squirrels.txt

cut -f6 tompkins_square_park_squirrels.txt

# using pipes and unique to help out
cut -f6 tompkins_square_park_squirrels.txt | uniq

cut -f6 tompkins_square_park_squirrels.txt | sort | uniq

# what activities were the squirrels observed doing?
cut -f12 tompkins_square_park_squirrels.txt | sort | uniq

# How many gray squirrels are there?
grep -c "gray" tompkins_square_park_squirrels.txt
0

grep -c "Gray" tompkins_square_park_squirrels.txt
55

grep -o "Gray" tompkins_square_park_squirrels.txt

grep -o "Gray" tompkins_square_park_squirrels.txt | wc -l

grep -o "Gray" tompkins_square_park_squirrels.txt | grep -c "Gray"

# What if a squirrel is black but with gray highights?
cut -f6 tompkins_square_park_squirrels.txt | grep -c "Gray"

# How many black squirrels?
grep -c "Black" tompkins_square_park_squirrels.txt

# How many cinnamon squirrels?
grep -c "Cinnamon" tompkins_square_park_squirrels.txt

# How many squirrels of each color in one command?
cut -f6 tompkins_square_park_squirrels.txt | sort | uniq -c
```

Combining files

```bash
# Make a file for all the squirrels in central manhattan
cat * > central_manhattan_squirrels.txt

ls

wc -l * # do the counts add up?

# they do, but we don't want them to
less central_manhattan_squirrels.txt

# each individual file has headers, but we only want one header in the new file
head -1 madison_square_park_squirrels.txt

# both print to standard out, we'll use it to our advantage
# overwrites the file
head -1 madison_square_park_squirrels.txt > central_manhattan_squirrels.txt

cat central_manhattan_squirrels.txt

# let's talk (briefly) about sed
man sed

sed '1d' madison_square_park_squirrels.txt

sed '1d' madison_square_park_squirrels.txt | wc -l

wc -l madison_square_park.txt

# make sure not to overwrite the file
for f in  *_park_squirrels.txt; do sed '1d' "$f" >> central_manhattan_squirrels.txt; done

wc -l central_manhattan_squirrels.txt

# Make a file for all of the squirrel data
cd .. # should be in squirrel_data now

ls

ls *

head -1 madison_square_park_squirrels.txt > all_park_squirrels.txt

for f in  */*_park_squirrels.txt; do sed '1d' "$f" >> all_park_squirrels.txt; done

wc -l all_park_squirrels.txt

wc -l */*_park_squirrels.txt

```

Some more practice

```bash
# How many squirrels in each of the parks?
wc -l all_park_squirrels.txt

# How many from each park?
cut -f3 all_park_squirrels.txt | sort | uniq -c

# Output the number of squirrels in each park as a text file
cut -f3 all_park_squirrels.txt | sort | uniq -c > num_squirrels_per_park.txt

# How many of each color?
cut -f6 all_park_squirrels.txt | sort | uniq -c

# How many were eating?
cut -f12 all_park_squirrels.txt | grep -c "Eating"
```

Comparing things from files

```bash
# Were there squirrels observed in every park?
cd .. # should be in bash_bootcamp

head park_data/park_info.txt

wc -l park_data/park_info.txt

# there are more parks in the park list than the squirrel list
# which parks don't have squirrel counts?
cut -f3 park_data/park_info.txt | sort > all_parks_list.txt

cut -f3 squirrel_data/all_park_squirrels.txt | sort | uniq > parks_with_squirrels.txt

comm -23 all_parks_list.txt parks_with_squirrels.txt

# parks with squirrels but not other data
comm -13 all_parks_list.txt parks_with_squirrels.txt

# parks in both places
comm -12 all_parks_list.txt parks_with_squirrels.txt
```


## 3. Working with Scripts

Write a script to count the number of squirrels in each park (in the individual files), cat the fies together, count the squirrels again, and check if they are the same.

Provide the script in case there is trouble with nano.  Windows users can also try Notepad as a backup.

Write a script that makes a new directory, makes a new file containing all of the squirrel data and only one header row, and answers these three questions using the new :

1. How many total squirrels were observed in NYC parks?
2. How many squirrels were observed in each park?
3. How many squirrels with each color combination (primary color + highlights) were observed?

Make the file and enter the editor.

```bash
touch squirrel_script.sh

ls

nano squirrel_script.sh
```

Script contents

```bash
#!/bin/bash

## make a new directory to store the data
mkdir combined_squirrel_data

## combine the smaller files
head -1 squirrel_data/central_manhattan/madison_square_park_squirrels.txt > combined_squirrel_data/all_squirrels_combined.txt

for f in squirrel_data/*/*_park_squirrels.txt
do
  sed '1d' "$f" >> combined_squirrel_data/all_squirrels_combined.txt
done

## total number of squirrels counted (plus one for the header)
wc -l combined_squirrel_data/all_squirrels_combined.txt

## number of each squirrels observed in each park
cut -f3 combined_squirrel_data/all_squirrels_combined.txt | sort | uniq -c

## number of squirrels of each color combination
cut -f6-7 combined_squirrel_data/all_squirrels_combined.txt | sort | uniq -c
```

Same script but prettier and more accurate

```bash
#!/bin/bash

## make a new directory to store the data
mkdir combined_squirrel_data

## make a file containing squirrel data from all parks
head -1 squirrel_data/central_manhattan/madison_square_park_squirrels.txt > combined_squirrel_data/all_squirrels_combined.txt

for f in squirrel_data/*/*_park_squirrels.txt
do
  sed '1d' "$f" >> combined_squirrel_data/all_squirrels_combined.txt
done

## count the number of squirrels in the new file
echo "----------------------------------------------------------------------"
printf "1. How many total squirrels were observed in NYC parks?\n\n"
printf "Total number of squirrels observed in NYC parks:\n\n"
sed '1d' combined_squirrel_data/all_squirrels_combined.txt | wc -l

## count the number of squirrels from each park
echo "----------------------------------------------------------------------"
printf "2. How many squirrels were observed in each park?\n\n"
printf "The number of squirrels in each park:\n\n"
sed '1d' combined_squirrel_data/all_squirrels_combined.txt | cut -f3 | sort | uniq -c

## How many squirrels of each color combination were observed?
echo "----------------------------------------------------------------------"
printf "3. How many squirrels with each color combination (primary color + highlights) were observed?\n\n"
printf "The number of squirrels observed with each color combination:\n\n"
sed '1d' combined_squirrel_data/all_squirrels_combined.txt |cut -f6-7 | sort | uniq -c
```