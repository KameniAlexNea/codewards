def is_pangram(s: str):
    import re
    s = "".join(re.findall("[a-z]*", s.lower()))
    return len(set(s)) == 26

if __name__ == "__main__":
    assert is_pangram("The quick, brown fox jumps over the lazy dog!")
    assert not is_pangram("1bcdefghijklmnopqrstuvwxyz")