
import csv
csvfile_russian = open('thing.csv', 'r', encoding = 'utf-8-sig')
host_reader = csv.reader(csvfile_russian, delimiter=',') #comma could be really anything
for row in host_reader:
    print(row[0], row[1])
csvfile_russian.close

# this is for the alphabet, I copied and pasted bc idk how csv works