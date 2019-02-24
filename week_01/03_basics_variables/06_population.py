'''
    In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds
    
    Write the necessary code to display the total population
    for the next 3 years (without a leap year).
    Let's say the current population is 380,123,456.
    
    '''

s = 365*24*3600

bornpery = s/6
diepery = s/12
impery = s/40

changepery = int(bornpery-diepery+impery)

print(changepery)

pop_3y = 380123456 + changepery * 3

print(pop_3y)