# super_market


In a normal supermarket, things are identified using Stock Keeping Units,. In our store, we’ll use individual letters of the alphabet (A, B, C, and so on). Our goods are priced individually. In addition, some items are multipriced: buy n of them, and they’ll cost you y Rs. For example, item ‘A’ might cost 50 Rs individually, but this week we have a special offer: buy three ‘A’s and they’ll cost you 120Rs. In fact this week’s prices are:

Item Unit Special

     Price     Price
A     50       3 for 120
B     30       2 for 45
C     20
D     15

Our checkout accepts items in any order, so that if we scan a B, an A, and another B, we’ll recognize the two B’s and price them at 45 . Because the pricing changes frequently, we need to be able to pass in a set of pricing rules each time we start handling a checkout transaction.
