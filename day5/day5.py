

def two_vent_count_straight(input_file: str) -> int:
    with open(input_file) as input:
        vents = {}
        for line in input:
            onetwo = line.split(' -> ')
            xyone = onetwo[0].split(',')
            xytwo = onetwo[1].split(',')
            x1 = int(xyone[0])
            y1 = int(xyone[1])
            x2 = int(xytwo[0])
            y2 = int(xytwo[1])
            
            # Check that it is vertical or horizontal
            if x1 == x2:
                if y1 < y2:
                    for y in range(y1,y2+1):
                        if vents.get((x1,y)):
                            vents[(x1,y)] += 1
                        else:
                            vents[(x1,y)] = 1
                else:
                    for y in range(y2,y1+1):
                        if vents.get((x1,y)):
                            vents[(x1,y)] += 1
                        else:
                            vents[(x1,y)] = 1
            elif y1 == y2:
                if x1 < x2:
                    for x in range(x1,x2+1):
                        if vents.get((x,y1)):
                            vents[(x,y1)] += 1
                        else:
                            vents[(x,y1)] = 1
                else:
                    for x in range(x2,x1+1):
                        if vents.get((x,y1)):
                            vents[(x,y1)] += 1
                        else:
                            vents[(x,y1)] = 1
            else:
                for diag_point in diag_generator(x1,y1, x2, y2):
                    if vents.get((diag_point[0], diag_point[1])):
                        vents[(diag_point[0], diag_point[1])] += 1
                    else:
                        vents[((diag_point[0], diag_point[1]))] = 1
            
        # print(vents)
        location_count = 0
        for location in vents:
            if vents[location] >= 2:
                # print(location, vents[location])
                location_count += 1
        return location_count

def diag_generator(x1, y1, x2, y2):
    diags = []
    if x1 > x2:
        deltax = -1
    else:
        deltax = 1
    if y1 > y2:
        deltay = -1
    else:
        deltay = 1
    for i in range(abs(x1-x2) + 1):
        x = x1 + deltax * i
        y = y1 + deltay * i
        diags.append((x, y))
    # print(diags)
    return diags

if __name__ == '__main__':
    print(two_vent_count_straight('input.txt'))