class SuperMarket:
    
    @classmethod
    def cal_bill(cls,cart):
        total_ammount = 0
       
        for prod,quantity in cart.items():
        	if prod.offer != None:
        		offer_avail = quantity // prod.offer.of_quantity
        		offer_price = offer_avail * prod.offer.offer_price
        		remain_quantity = quantity % prod.offer.of_quantity
        		remain_price = remain_quantity * prod.p_price
        		total_ammount += offer_price + remain_price
        	else:
        		total_ammount += prod.p_price * quantity

        	prod.update_stock(prod.p_quantity - quantity)
        	
        total_ammount += total_ammount * 0.05
        return total_ammount

