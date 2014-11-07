spare-change
============

This Python utility takes a transaction log from [Mint](https://www.mint.com) and produces the spare change left over from every transaction. The idea is to quickly get an amount you could manually put in savings. Inspired by tools like Bank of America's [Keep the Change](https://www.bankofamerica.com/deposits/manage/keep-the-change.go) or [Acorns](https://www.acorns.com/).

## Installation

The script only requires Python 2.7 and the [tabulate](https://pypi.python.org/pypi/tabulate) package. The easiest way to install is:

```shell
$ pip install --requirement requirements.txt
```

## Example Usage

The first step is to obtain the CSV of transactions from Mint. You can do this by:

1. Logging in at [Mint](http://www.mint.com/).
2. Selecting the "Transactions" tab at the top.
3. Scroll all the way to the bottom and click "Export all <number> transactions".

Here is an example of running the command and the output.

```shell
$ python spare_change.py transactions.csv
Month      2014    2013
-------  ------  ------
Jan       15.49   13.36
Feb       13.52   11.47
Mar       15.91   15.99
Apr        7.29   12.06
May        7.49   14.42
Jun       11.17   16.35
Jul        8.92   13.86
Aug       13.26   16.13
Sep       10.62   17.73
Oct       14.14   15.38
Nov               16.87
Dec               20.15
Total    117.79  183.77
```
