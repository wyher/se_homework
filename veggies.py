veggies = {'cabbage':120, 'carrot':230, 'spinach':100, 'asparagus':190,'artichoke':670,'lettuce':300}

total = 0

for price in veggies.values():
	total += price
print(total)