#Man in the well.
#A man is stuck at the bottom of a well. Each day, he climbs up
#8 meters, and then at night, he slips downwards by 3 meters.
#Using loops(any loop of your choice), write a function to determine
#(and print) how many days and nights it takes for him to climb out of a well
#of any given depth, where the depth of the well is taken as input.
#e.g: f(17) => the well is 17 meters deep.
#Day 1: climbs 8m, height = 8m; slips 3m, height = 8-3 = 5m;
#Day 2: climbs 8m, height = 5+8 = 13m; slips 3m, height = 13-3 = 10m;
#Day 3: climbs 8m, height = 10+8 = 18m. 
#But 18>17. STOP(height climbed has exceeded well depth)
#Therefore, f(17) = 3days

depth = int(input('Enter the depth of the well in meters(e.g; 7): '))

def climbing_days(depth):
    height_climbed = 0
    days = 0
    nights = 0
    while height_climbed < depth:
        height_climbed += 8
        days += 1
        if height_climbed < depth:
            height_climbed -= 3
            nights += 1
    return days, nights

print('It will take ', (climbing_days(depth))[0], 'days, ' , (climbing_days(depth))[1], 'nights to climb the well.', sep='')