def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    s = s[1:-1]
    return is_palindrome(s)

if __name__ == '__main__':
    # racecar
    assert is_palindrome('racecar') == True
    assert is_palindrome('cat') == False