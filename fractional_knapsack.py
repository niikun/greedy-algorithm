from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    values_per_weights = [v/w for v,w in zip(values, weights)]
    combined = list(zip(weights,values_per_weights))
    combined.sort(key=lambda x: x[1],reverse=True)
    weights,values_per_weights = zip(*combined)
    for w,vpw in zip(weights,values_per_weights):
        if capacity-w >= 0:
            capacity -= w
            value += vpw*w
  
        else:
            w = capacity
            value += vpw*w
            break

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
