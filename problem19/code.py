f = open('testinput.txt', 'r')

beacons = []
for x in f:
    x = x.rstrip()
    if x.count(",")==2:
        beacons[-1].append(tuple(map(int,x.split(','))))
    elif len(x) !=0:
        beacons.append([])

def matchbeacons(beacons, pairs, ordering):
    if len(pairs) == 12:
        return pairs[0][0][0], pairs [0][1][0]
    elif len(pairs) == 0:
        #loop through all beacon pairs
        pass
    else:
        beacon1 = pairs[0][0][0]
        beacon2 = pairs[0][1][0]
        for location in list(filter(lambda x: x not in [y[0][1] for y in pairs], beacons[beacon1])):
            for location2 in list(filter(lambda x: x not in [y[1][1] for y in pairs], beacons[beacon2])):
                