def height(n, m):
    """
    :param n: the number of people
    :param m: the number of bananas
    :return: the height of the pyramid
    """
    # Write your code here
    return m * pow(2, n, MOD) % MOD

# The following code is used to test the function:

from solution import height
import codewars_test as test

@test.describe('Example tests')
def desc1():
    @test.it("should work for some basic tests")
    def it1():
        test.assert_equals(height(1,51),51)
        test.assert_equals(height(2,1),1)
        test.assert_equals(height(4,17),3213)
        test.assert_equals(height(16,19),524096)
        test.assert_equals(height(23,19),524287)
    @test.it("should work for some advanced tests")
    def it2():
        test.assert_equals(height(13,550),621773656)
        test.assert_equals(height(531,550),424414512)
    @test.it("should work for some serious tests :)")
    def it3():
        test.assert_equals(height(10 ** 4, 10 ** 5),132362171)
        test.assert_equals(height(8*10 ** 4, 10 ** 5),805097588)
        test.assert_equals(height(3000,2 ** 200),141903106)
        test.assert_equals(height(8*10 ** 4, 4*10 **4 ),616494770)
        test.assert_equals(height(4*10 ** 4, 8*10 ** 4),303227698)