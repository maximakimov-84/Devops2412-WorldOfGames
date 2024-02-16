def is_valid_integer(s):
    if s.isdigit():
        return True
    elif s[0] == '-' and s[1:].isdigit():
        return True
    return False