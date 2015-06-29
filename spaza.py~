
import csv

def productList():
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

    return things

def mostPopularProduct(things):
    my_max_val = 0
    for product,amount in things.items():
        if amount > my_max_val:
            my_max_val=amount
            my_max_key=product
            mostPopular = {
            'product' : my_max_key,
            'qty' : my_max_val
    
            }
    return mostPopular

def leastPopularProduct(things):
    my_min_val = 172
    for product,amount in things.items():
        if amount < my_min_val:
            my_min_val=amount
            my_min_key=product
            leastPopular = {
            'product' : my_min_key,
            'qty' : my_min_val
    
            }
    return leastPopular

product = productList()
print "PRODUCT LIST"
print productList()
print "=========================="
print "MOST POPULAR PRODUCT"
print mostPopularProduct(product)
print "=========================="
print "LEAST POPULAR PRODUCT"
print leastPopularProduct(product)


 
