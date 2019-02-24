'''
    If a runner runs 12 kilometers in 30 minutes and 30 seconds.
    What is his/her average speed in miles per hour. (Tip: 1 mile = 1.6 km)
    
    '''
km = 12
miles = 12 * 1.6
minutes = 30
seconds = 30

hours = minutes/60 + seconds/60**2

speedkm = km/hours

print(speedkm)
