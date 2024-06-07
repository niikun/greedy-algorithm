def greedy_coin(amount):
    if amount <= 0:
        return {}

    coins = [0.25, 0.10, 0.05, 0.01]
    coin_lookup = {0.25: "quarter", 0.10: "dime", 0.05: "nickel", 0.01: "penny"}
    coin_dict = {}
    remaining_amount = amount

    while remaining_amount > 0:
        for coin_value in coins:
            if remaining_amount >= coin_value:
                remaining_amount -= coin_value
                remaining_amount = round(remaining_amount, 2)
                coin_name = coin_lookup[coin_value]
                if coin_name not in coin_dict:
                    coin_dict[coin_name] = 1
                else:
                    coin_dict[coin_name] += 1
                break

    return coin_dict

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            input_amount = float(sys.argv[1])
            result = greedy_coin(input_amount)
            for coin, count in result.items():
                print(f"{count} {coin}(s)")
        except ValueError:
            print("Please provide a valid number for the amount.")
    else:
        print("Please provide an amount as a command-line argument.")
