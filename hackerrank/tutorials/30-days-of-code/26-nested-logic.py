#!/bin/python3
import datetime

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def convertToDate(orig):
    arr = orig.split(' ')
    return datetime.datetime(int(arr[2]), int(arr[1]), int(arr[0]))

if __name__ == '__main__':
    actual_date = input()
    expected_date = input()
    actual_date = convertToDate(actual_date)
    expected_date = convertToDate(expected_date)
    if expected_date > actual_date:
        print(0)
    elif expected_date.month == actual_date.month and expected_date.year == actual_date.year:
        print(15*(actual_date-expected_date).days)
    else:
        months_diff = diff_month(actual_date, expected_date)
        if expected_date.year != actual_date.year:
            print(10000)
        elif months_diff < 12:
            print(500*months_diff)
    
    