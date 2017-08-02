from string import Template

def main():
	cart=[]
#	get_price = raw_input("Enter the price")
	cart.append(dict(item="BOVONTO",price=2,qty=2))
	cart.append(dict(item="Ground Nuts",price=3,qty=50))
	total=0
	t = Template("$item * $qty = $price")
	print "Cart"
	for data in cart:
		print t.substitute(data)
		total += data["price"]
	print "Total  " + str(total)
		

if __name__ == "__main__":
	main()
		
	
