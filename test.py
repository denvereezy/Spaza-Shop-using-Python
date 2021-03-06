import spaza
import unittest
productMap = spaza.productList()
mostPopularPdt = spaza.mostPopularProduct(productMap)
leastPopularPdt = spaza.leastPopularProduct(productMap)

class MyTest(unittest.TestCase):
    def test_mostPopularProduct(self):
    	print mostPopularPdt
        self.assertEqual('Mixed Sweets 5s', mostPopularPdt['product'])
        self.assertEqual(172, mostPopularPdt['qty'])

    def test_leastPopularProduct(self):
    	print leastPopularPdt
    	self.assertEqual('Valentine Cards', leastPopularPdt['product'])
        self.assertEqual(14, leastPopularPdt['qty'])

if __name__ == '__main__':
    unittest.main()
