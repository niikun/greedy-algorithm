def min_refills(distance, tank, stops):
    refills = 0
    current_position = 0
    stops = [0] + stops + [distance]

    for i in range(1, len(stops)):
        if stops[i] - stops[i-1] > tank:
            return -1
        
        if stops[i] > current_position + tank:
            refills += 1
            current_position = stops[i-1]

    return refills

