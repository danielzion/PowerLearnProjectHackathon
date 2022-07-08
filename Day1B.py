sqr_feet =  float(input('Please enter the Square Feet of wall to be painted: '))
paint_price = float(input('What is the price of paint per gallon: '))

ratio = (sqr_feet/115)

no_of_gallons = ratio

no_of_hours = (8 * ratio)

cost_of_paint = (paint_price * no_of_gallons)

labour_cost = (no_of_hours * 20)

total_cost = (labour_cost + cost_of_paint)

print(f'The number of gallons of paint required is {no_of_gallons} gallons')
print(f'The hours of labour required is {no_of_hours} hours')
print(f'The cost of the paint is ${cost_of_paint}')
print(f'The labour charges is ${labour_cost}')
print(f'The total cost of the paint job is ${total_cost}')