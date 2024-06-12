from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    refills = 0
    temp_m = m

    for i in range(len(stops)):
        
        if i == 0:
            temp_m -= stops[i]
            # print(temp_m)

            if temp_m < stops[i+1]-stops[i]:
                refills += 1
                temp_m = m
                # print("refile")
                if temp_m < stops[i+1]-stops[i]:
                    refills = -1
                    break

        elif i < len(stops)-1:
            temp_m = temp_m - stops[i]+stops[i-1]
            # print(temp_m)

            if temp_m < stops[i+1]-stops[i]:
                refills += 1
                temp_m = m
                # print("refile")
                if temp_m < stops[i+1]-stops[i]:
                    refills = -1
                    break

        else:
            temp_m = temp_m - stops[i]+stops[i-1]
            # print(temp_m)

            if temp_m < d-stops[i]:
                refills += 1
                temp_m = m
                # print("refile")
                if temp_m < d-stops[i]:
                    refills = -1
                    break
    return refills

    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
