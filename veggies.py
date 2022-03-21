veggies = {'cabbage':12, 'carrot':23, 'spinach':10, 'asparagus':19,'artichoke':67,'lettuce':30}

total = 0

for price in veggies.values():
	total += price
print(total)