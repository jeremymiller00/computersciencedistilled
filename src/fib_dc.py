import time

M = {}
M[1] = 1
M[2] = 2

def fib_recursive(n):
    if n <= 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_dp(n):
    if n not in M.keys():
        M[n]  = fib_dp(n-1) + fib_dp(n-2)
    return M[n]

def compare(n):
    r_start = time.time()
    rec = fib_recursive(n)
    r_end = time.time()

    d_start = time.time()
    dp = fib_dp(n)
    d_end = time.time()

    print(f"Time elapsed for recursive fib({n}):")
    print(f"{r_end-r_start}")
    print(f"Time elapsed for dynamic fib({n}):")
    print(f"{d_end-d_start}")

############

if __name__ == '__main__':
    # 1,1,2,3,5,8,13
    assert fib_recursive(3) == 2
    assert fib_recursive(7) == 13
    compare(10)