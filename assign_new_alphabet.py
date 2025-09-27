
import csv
import xlsx
import pandas


new_alphabet = pandas.read_excel(r'C:\Users\leenglis\OneDrive\Artificial_Language\Alphabet.xlsx', engine='openpyxl')

# Print the first 2 columns of every row
for index, row in new_alphabet.iterrows():
    print(row[0], row[1]) # this line is just for testing


#csvfile_russian = open('Alphabet.csv', 'r', encoding = 'utf-8-sig')
#host_reader = csv.reader(csvfile_russian, delimiter=',') # comma could be really anything
#for row in host_reader:
#    print(row[0], row[1])
#csvfile_russian.close

# only God knows what this was^^ I don't remember
# alphabet is still being worked on, custom letters will be added in first column with LaTeX at some point
