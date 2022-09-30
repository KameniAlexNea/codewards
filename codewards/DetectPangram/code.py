def is_pangram(s: str):
    import re
    s = "".join(re.findall("[a-z]*", s.lower()))
    return len(set(s)) == 26