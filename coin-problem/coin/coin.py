from typing import List
import math

coins = [2.0, 1.0, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

class Coin:
    @staticmethod
    def get_coins(money: float) -> List[float]:
        result = []
        for key, value in enumerate(coins):
            try:
                if money >= value:
                    fraction, whole = math.modf(money/value)
                    adding = [value] * int(whole)
                    result.extend(adding)
                    if fraction == 0:
                        break
                    else:
                        money = round(money - (value * whole), 2)
            except TypeError as type_error:
                print(type_error)
        return result


