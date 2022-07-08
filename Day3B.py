no_of_fat_g = float(input('What is the number of fat grams consumed: '))
no_of_carb_g = float(input('What is the number of Carbohydrate grams consumed: '))

fat_cal = (no_of_fat_g * 9)
carb_cal = (no_of_carb_g * 4)

total_no_of_cal = (fat_cal + carb_cal)

print(f"The number of calories resulting from fats is {fat_cal}\n"
        f"The number of calories resulting from carbohydrates is {carb_cal}\n"
        f"The total number of calories is {total_no_of_cal}")