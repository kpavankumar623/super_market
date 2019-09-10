
class Offers:
	 def __init__(self, of_id,p_id, of_quantity, offer_price, valid_date):
	 	self.of_id = of_id
	 	self.p_id = p_id 
	 	self.of_quantity = of_quantity
	 	self.offer_price = offer_price
	 	self.valid_date = valid_date

	 def remove_offer(self):
	 	id = self.id
	 	del self
	 	return id 

	 def update_offer_quantity(self,new_quntity):
	 	self.of_quantity = new_quntity
	 	
	 def update_offer_price(self,new_price):
	 	self.offer_price = new_price

	 
