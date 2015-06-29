import spaza
from spaza import productList

productMap = productList()

print "PRODUCT LIST"
print spaza.productList()
print "===================="
print "MOST POPULAR PRODUCT"
print spaza.mostPopularProduct(productMap)
print "===================="
print "LEAST POPULAR PRODUCT"
print spaza.leastPopularProduct(productMap)

    


