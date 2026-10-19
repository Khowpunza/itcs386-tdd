# shipping.py 
"""Return the shipping fee in baht for a parcel of weight_kg kilograms. 
Rule 1. The weight must be more than 0 kg. Otherwise raise ValueError. 
Rule 2. A parcel of up to 1 kg costs 40 baht. 
Rule 3. A parcel of more than 1 kg and up to 5 kg costs 60 baht. 
Rule 4. A parcel of more than 5 kg costs 60 baht plus 10 baht for every 
started kilogram above 5 kg. A 5.2 kg parcel costs 70 baht. 
""" 
import math


def shipping_fee(weight_kg): 
    #fix by add <= to the condition to make sure that weight_kg is more than 0 kg
    if weight_kg <= 0: 
        raise ValueError("weight must be more than 0 kg") 
    # fix by add <= to the condition to make sure that weigth in the range 1
    if weight_kg <= 1: 
        return 40 
    if weight_kg <= 5: 
        return 60 
    # Bug 3 Fix: Replaced int() with math.ceil() to charge for every *started* kg
    extra = math.ceil(weight_kg - 5)
    return 60 + 10 * extra 