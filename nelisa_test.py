#import sys

#read_raw_file = open('558ba7f86373761020010000.csv') # open current file
#read_raw_text  = read_raw_file.read()
#new_text = read_raw_text.strip()

#new_text = new_text.replace(';','\t')

#text_list = new_text.split('\r')
#unique_items = []


#for row in text_list:
 #   if row not in unique_items:
  #      unique_items.append(row)

#print row

import csv

f = open('sales.csv')
csv_f = csv.reader(f) 

# create an empty map first...
things = {}
for row in csv_f:
    currentItem = row[2]
    numberSold =  row[3]
    # check if the item is already in the map
    if not things.has_key(currentItem): 
        things[currentItem] = 0
    things[currentItem] += int(numberSold)

print things

def productList()

#for item,qty in things.items():
 #print item, "=>", qty


 
