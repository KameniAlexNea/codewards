from codewards.DetectPangram.code import is_pangram

def test_case0():
    assert is_pangram("The quick, brown fox jumps over the lazy dog!")

def test_case1():
    assert not is_pangram("1bcdefghijklmnopqrstuvwxyz")