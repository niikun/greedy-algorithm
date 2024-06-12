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



