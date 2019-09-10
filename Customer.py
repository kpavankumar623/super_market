import SuperMarket as sp
class Customer:
    def __init__(self,c_id,c_name,c_contact,c_cart = {}):
        self.c_id = c_id
        self.c_name = c_name
        self.c_contact = c_contact
        self.c_cart = c_cart
        
    def add_to_cart(self,prod,quantity):
        if prod in self.c_cart:
            self.c_cart[prod]= self.c_cart[prod] + quantity
        else:
            self.c_cart.setdefault(prod,quantity)
            
    def remove_from_cart(self,prod):
        if prod in self.c_cart:
            id = prod.p_id
            self.c_cart.pop(prod)
            return id
        
    def req_bill(self):
        return sp.SuperMarket.cal_bill(self.c_cart)
