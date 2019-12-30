#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22, 2019 09:43:46 AM
@author: eapetcho
"""
import argparse
import os


def read_cmdline():
    """Read the command line.

    Returns
    -------
    args: dict, argparse.Namespace object
        Encapsulate the argument entered on the commandline by the
        user.
    info: str
        Help message on how to use this program.
    """
    parser = argparse.ArgumentParser(
        description="Exctract a clip from a video file")
    parser.add_argument('--outfile', type=str,
                        help="Output file name")
    parser.add_argument("--infile", type=str,
                        help="Input file name")
    parser.add_argument("--start", type=str,
                        help="Start time in the input video (HH:MM:SS)")
    parser.add_argument("--duration", type=str,
                        help="Duration of the output video file"
                        " (HH:MM:SS)")
    args =  parser.parse_args()
    with open("tmp.txt", "w") as fd:
        parser.print_help(file=fd)

    info = ""
    with open("tmp.txt", "r") as fd:
        info = fd.read()

    #if os.path.exists("tmp.xtx"):
    os.system("rm -f tmp.txt")

    return args, info


def parse_cmdline():
    """Parse the command line argument.

    Returns
    -------
    args: dict, argparse.Namespace object
        agument entered at the commandline

    Raises
    ------
    AttributeError
    """
    args, info = read_cmdline()
    if not args.outfile:
        print(info)
        raise AttributeError("\nMissing output file")
    if not args.infile:
        print(info)
        raise AttributeError("\nMissing input file")
    if not args.start:
        print(info)
        raise AttributeError("\nMissing starting time")
    if not args.duration:
        print(info)
        raise AttributeError("\rMissing duration")

    return args

def extractor():
    """
    Extract the requested video clip from the input video file
    """
    args = parse_cmdline()
    START = args.start
    DURATION = args.duration
    INPUT = args.infile
    OUTPUT = args.outfile

    cmd = f"ffmpeg -ss {START} -i {INPUT} -t {DURATION} -vcodec"
    cmd = cmd + f" copy -acodec copy {OUTPUT}"
    os.system(cmd)

def prologue():
    pass



if __name__ == "__main__":
    # args = parse_cmdline()
    extractor()
