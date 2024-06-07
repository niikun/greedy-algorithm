# %!/usr/bin/env python3
import click


def greedy_coin(amount):

    coins = [0.25, 0.10, 0.05, 0.01]
    coin_lookup = {0.25: "quarter", 0.10: "dime", 0.05: "nickel", 0.01: "penny"}
    coin_dict = {}
    while amount > 0:
        for coin in coins:
            if amount >=coin:
                amount -= coin
                amount = round(amount,2)
                coin_name = coin_lookup[coin]
                if coin_name not in coin_dict.keys():
                    coin_dict[coin_name]=1
                else:
                    coin_dict[coin_name] +=1
                break

    return coin_dict


@click.command()
@click.argument("amount",type=float)
def main(amount):
    """
    Enter the amount to be converted into coins
    """
    print(greedy_coin(float(amount)))

if __name__=="__main__":
    main()