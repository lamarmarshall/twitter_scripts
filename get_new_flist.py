import os
import time
import datetime
import sys

#tm = time.ctime()

def file_age_in_hours(filename):
    timestamp_str = datetime.datetime.fromtimestamp(os.stat(filename).st_mtime).strftime('%Y-%m-%d-%H:%M')

    print(  timestamp_str )
    hours_since = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.stat(filename).st_mtime)
    return round(hours_since.seconds / 60 /60 ) 

if __name__ == '__main__':

    filename="followers.txt"
    try:
        if sys.argv[1] != None:
            filename = sys.argv[1]
    except IndexError:
        pass

    age = file_age_in_hours(filename)
    print(filename + " is (" + str(age) + ") hours old")