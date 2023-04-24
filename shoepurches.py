#!/bin/python3

from Shoes import Shoes

low = Shoes("And 1s", 30)
mid = Shoes("Air Forces 1s", 120)
high = Shoes("Off Whites", 400)

try: 
	shoe_budget = float(input("What is your shoe budget? "))
except ValueError: 
	exit("Please Enter A Number")

for shoes in [high, mid , low]:
	shoes.buy(shoe_budget)
	
