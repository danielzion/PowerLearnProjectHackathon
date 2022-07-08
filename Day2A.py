
def main():
    try:
        customer_purchase = int(input('Please enter the number of books you purchased this month '))

    except ValueError as error:
        print('Invalid Number of purchase')

    else:
        if customer_purchase == 0:
            pts = 0 
        elif customer_purchase == 1:
            pts = 6
        elif customer_purchase == 2:
            pts = 16
        elif customer_purchase == 3:
            pts = 32
        elif customer_purchase >= 4:
            pts = 60
    print(f"You have been awarded {pts} points")

while True:
    main()