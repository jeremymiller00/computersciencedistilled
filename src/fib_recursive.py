def fib_recursive(n):
    if n <= 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

############

if __name__ == '__main__':
    # 1,1,2,3,5,8,13
    assert fib_recursive(3) == 2
    assert fib_recursive(7) == 13