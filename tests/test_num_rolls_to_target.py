from codewards.NumRowsToTarget.code import Solution


def test_case1():
    assert Solution().numRollsToTarget(
        2, 6, 7
    ) == 6

def test_case2():
    assert Solution().numRollsToTarget(
        3, 7, 12
    ) == 37