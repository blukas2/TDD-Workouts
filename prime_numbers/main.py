import timeit

def is_prime(x):
    if (x == 0) or dividable_by_any(x):
        return False
    else:
        return True
    
def dividable_by_any(x):
    n = 2
    while n<x:
        dividable = (x/n == x//n)
        if dividable:
            return True
        n += 1 
    else:
        return False


if __name__ == "__main__":
    starttime = timeit.default_timer()
    print(is_prime(2147483647))
    duration = timeit.default_timer() - starttime
    print(f"Print runtime: {duration}")