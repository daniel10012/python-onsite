'''
    Celsius to Fahrenheit:
    
    Write the necessary code to read a degree in Celsius from the console
    then convert it to fahrenheit and print it to the console.
    
    F = C * 1.8 + 32
    
    Output should read like - "27.4 degrees celsius = 81.32 degrees fahrenheit"
    
    NOTE: if you get an error, look up what input() returns!
    
    '''


def fahrenheit(c):
    f = int(c*1.8 + 32)
    return f

c = int(input("Degrees Celcius:"))



print(f"{c} degrees celcius = {fahrenheit(c)} degrees fahrenheit")