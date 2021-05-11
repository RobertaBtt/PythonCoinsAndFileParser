from coin import coin
if __name__ == '__main__':
    coins_total_amount: float = None


    print("Hi, insert the float amount \n(. as decimal separator)")
    try:
        coins_total_amount = float(input())
    except ValueError as value_error:
        print(value_error, ", \nRun again")


    if coins_total_amount is not None:
        print(coin.Coin.get_coins(coins_total_amount))
