

import pytest
from codewards.freq_most_freq.code import Solution


def test_max_frequency():
    res = Solution().maxFrequency(
        [1,1,1,2,5,4,7,8,56,7,8,4,7,7,7,4,5,8,9,6,6,6,3,2,4,5,7,7,7,7,7,10,10,12,12,12,11,11,11,11,4],
        50
    )
    assert res == 26

def test_max_frequency2():
    res = Solution().maxFrequency(
        [9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,
        9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,
        9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,
        9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,
        9936,9975,9954,9932,9964,9972,9935,9946,9966], 
        3056
    )
    assert res == 73

@pytest.mark.timeout(0.1)
def test_max_frequency3_rand():
    import random
    random.seed(12345)
    res = Solution().maxFrequency(
        [random.randint(9000, 10000) for _ in range(10000)],
        10000
    )
    print(res)
