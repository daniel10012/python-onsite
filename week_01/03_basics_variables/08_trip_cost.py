'''
    Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel
    
    Display the cost of the trip in the console.
    
    '''

miles = int(input("miles to drive"))
MPG = int(input("MPG of the car"))
Price_pg = int(input("price per gallon"))

print(miles/MPG*Price_pg)