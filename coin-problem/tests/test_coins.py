from coin import coin
from coin import coin_golf
from unittest import TestCase


class CoinTest(TestCase):

    def testExample(self):
        assert(coin.Coin.get_coins(2.34) == [2.0, 0.20, 0.10, 0.02, 0.02])

    def testZero(self):
        assert(coin.Coin.get_coins(0.0) == [])

    def testMinus(self):
        assert(coin.Coin.get_coins(-1) == [])

    def testError(self):
        self.assertRaises(TypeError, coin.Coin.get_coins("ciao"))

    def testString(self):
        assert(coin.Coin.get_coins("0.9") == [])

    def testNine(self):
        assert(coin.Coin.get_coins(9) == [2,2,2,2,1])

    def testCoinGolf(self):
        assert(coin_golf.get_coins(2.34) == [2.0, 0.20, 0.10, 0.02, 0.02])