import prime
# import unittest

# class Test_IsPrime(unittest.TestCase):
#         def test_check_prime(self):
#                 self.assertEqual(prime.checkPrimality(1) , False)
#                 self.assertEqual( prime.checkPrimality(2),  True)
#                 self.assertEqual( prime.checkPrimality(3) , True)
#                 self.assertEqual( prime.checkPrimality(4) , False)
#                 self.assertEqual( prime.checkPrimality(5) ,False)
#                 self.assertEqual( prime.checkPrimality(6) , False)
                
# if __name__ == '__main__':
#         unittest.main()


def test_check_prime():
        assert prime.checkPrimality(1) == False
        assert prime.checkPrimality(2)==  True
        assert prime.checkPrimality(3)== True
        assert prime.checkPrimality(4) == False
        assert prime.checkPrimality(5) ==True
        assert prime.checkPrimality(6) == False

test_check_prime()
