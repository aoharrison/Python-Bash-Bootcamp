#!/usr/bin/env python

# Example: ./seq_length_stats.py seqs.fasta boxplot.png

import os.path
import sys

import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO


def coefficient_of_variation(ary):
    """Coefficient of variation: ratio of std to the mean."""
    return np.std(ary) / np.mean(ary)


def summarize(ary):
    mean = np.mean(ary)
    std = np.std(ary)
    coef = coefficient_of_variation(ary)

    return (mean, std, coef)


def print_summary(summary):
    # Note summary can be a tuple, list, etc.
    rounded = [round(x, 2) for x in summary]

    # Splat is what it's called in Ruby...not sure about Python.
    # But it's used to "unpack" the tuple/list/collection.
    print(*rounded, sep=" -- ")


def read_seq_lengths(file_name):
    if not os.path.exists(file_name):
        print(f'ERROR: file "{file_name}" does not exist!')
        sys.exit(1)

    file_format = "fasta"

    lengths = [len(record.seq)
               for record in SeqIO.parse(file_name, file_format)]

    return np.array(lengths)


def parse_argv(argv):
    """Parse command line arguments.

    This is so simple we probably wouldn't bother.  But if you had complicated 
    arg parsing, it would be good to keep it separate."""

    # Check the args.
    if len(argv) != 3:
        print(f'usage: {argv[0]} <input_seqs> <output>', file=sys.stderr)
        sys.exit(1)

    return {
        'seqs_file': argv[1],
        'boxplot_file': argv[2]
    }


def write_boxplot(ary, out_name):
    figure, axis = plt.subplots()

    axis.boxplot(ary, vert=False)

    plt.xlabel('Sequence Length')

    plt.savefig(out_name)


def main():
    args = parse_argv(sys.argv)

    lengths = read_seq_lengths(args['seqs_file'])

    summary = summarize(lengths)

    print_summary(summary)

    write_boxplot(lengths, args['boxplot_file'])


# __name__ will be set to different things depending on the context in which
# this script is run.  https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    main()
