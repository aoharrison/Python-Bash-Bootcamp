# Script readme

There is a lot of new information in this script.  You do not need to understand it all right now.  You will be discussing plotting and numpy in the AI/ML workshop.  If you would like to get a head start on understanding the plotting, [this](http://swcarpentry.github.io/python-novice-gapminder/09-plotting/index.html) is a great resource to check out.

The other unfamiliar things in this script (reading input from the command line and defining main) are very common things in python.  You will not be doing this in the workshop, but I thought it would be good for you to see them.

**I will be making a video that will walk you through this script.**  So, you do not need to run it.  However, if you want to run it, here are the instructions.

## Installing libraries

If you did not install Anaconda, you will need to install Biopython, numpy, and matplotlib.

* [Biopython instructions](https://biopython.org/wiki/Download)
* [Numpy instructions](https://numpy.org/install/)
* [Matplotlib instructions](https://matplotlib.org/stable/users/installing/index.html)

## About the script

The script takes a fasta file and calculates the mean, standard deviation, and coefficient of variation of the lengths of all of the sequences.  Then, it makes a box and whisker plot of this data and saves it as a png for you to view.

## Running the script

Launch Jupyter Lab, navigate to the folder `example_script`, and open up a terminal.  Now, run the script the same way you would on the regular command line.  Remember to include the command line arguments required by the script.  Use the `also_fruit.fasta` file first so you don't overwrite the other example (this `also_fruit.fasta` is slightly different from `fruit.fasta` in that the sequences are different lengths).

Before running the script, make sure you are in the same directory as the script and the data.

Windows and Linux users should run:

```bash
python seq_length_stats.py also_fruit.fasta fruit_box.png
```

MacOS users should run:

```bash
python3 seq_length_stats.py also_fruit.fasta fruit_box.png
```
The only difference is `python3` instead of just `python`

## Output

If all goes well, you should end up with 3 floats printed to your screen representing the mean, standard deviation, and coefficient of variation of the sequence lengths and a brand new png called `fruit_box.png` with a lovely box and whisker plot.