#!/usr/bin/env python

#from ..utils import transformcsv
import os, sys
import argparse


# Don't mess with anything else below here
#------------------------------------------------------------

def output_report(report, folder_path):
    report_path = os.path.join(folder_path, 'report.txt')
    f = open(report_path, 'w')
    f.write('\r\n'.join(report))
    f.close()


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=int,
                        help="display a square of a given number")
    parser.add_argument("output_folder_path",
                        help="output_folder_path")
    args = parser.parse_args()
    report = transformcsv(args.csv_file, args.output_folder_path)
    output_report(report, args.output_folder_path)

if __name__ == "__main__":
    if __package__ is None:
        from os import sys, path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from utils import transformcsv
    else:
        from utils import transformcsv
    main (sys.argv)