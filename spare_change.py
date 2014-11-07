import argparse
import calendar
import collections
import csv
import datetime
import math
import os
import sys
from tabulate import tabulate

MONTHS_IN_YEAR = 12

def main():
    parser = argparse.ArgumentParser(
        description='Finds spare change using CSV exported from Mint!')
    parser.add_argument('filename', type=str,
        help='Filename to read for csv.')
    parser.add_argument('-y', '--years', type=int, default=5,
        help='The number of previous years (including current) to print.')

    args = parser.parse_args()

    # Ensure that the file exists that user provides.
    if not os.path.isfile(args.filename):
        print "ERROR: {0} does not exist! Please specify a valid file!".format(
            args.filename)
        sys.exit(1)

    # Determine the start date for grabbing the values.
    TODAY = datetime.datetime.now()
    start_date = datetime.datetime(
        TODAY.year - args.years + 1,
        1,
        1)

    spare_change = collections.OrderedDict(
        {"Month" : calendar.month_abbr[1:13] + ["Total"]})

    # Open the CSV file and parse each row.
    with open(args.filename, 'rb') as csvfile:
        dictreader = csv.DictReader(csvfile)
        for row in dictreader:
            date = datetime.datetime.strptime(row['Date'], '%m/%d/%Y')

            # If the date is greater than the start date, accumlate values.
            if date > start_date:

                # See if the year exist in the dictionary yet and create
                # the list if not. We use None here instead of 0 so the table
                # does not print values that are zero.
                if date.year not in spare_change:
                    spare_change[date.year] = [None] * (MONTHS_IN_YEAR + 1)

                # Calculate the change and then add the amount to the list
                # in the dictionary. Index is the month offset by 1 since
                # the list starts with 0.
                dollars = float(row['Amount'])
                change = dollars - math.floor(dollars)

                if spare_change[date.year][date.month - 1] is None:
                    spare_change[date.year][date.month - 1] = change
                else:
                    spare_change[date.year][date.month - 1] += change

                if spare_change[date.year][12] is None:
                    spare_change[date.year][12] = change
                else:
                    spare_change[date.year][12] += change


    # Print the results.
    print tabulate(spare_change, headers="keys", floatfmt=".2f")

if __name__ == '__main__':
    main()


