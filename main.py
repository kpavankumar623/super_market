import Product as pro
import Customer as cus
import Offers as off

p1 = pro.Product(101,"A",50,500)
p2 = pro.Product(102,"B",30,50)
p3 = pro.Product(103,"C",20,500)

offer1 = off.Offers(11,101,3,120,'04 oct 19')
offer2 = off.Offers(12,102,2,45,'23 sep 19')

p1.add_offer(offer1)
p2.add_offer(offer2)


c1 = cus.Customer(1,"ABC","+914789988")

c1.add_to_cart(p1,3)
c1.add_to_cart(p2,5)
c1.add_to_cart(p1,2)
c1.add_to_cart(p3,1)


print(c1.req_bill())
print(p1.p_quantity)
print(p2.p_quantity)