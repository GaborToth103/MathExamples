import mpmath
import math
import numpy as np
import time
import logging

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"{func.__name__} took {elapsed_time:.6f} seconds to run.")
        return result
    return wrapper

def log_results(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned: {result}")
        return result

    return wrapper



@log_results
def feladat_1(times: int, base: int):
    """ (1.2) Checks the difference between powers and multiplication in Python. We measure the time between them.

    Args:
        times (int): the number of times to do the arithmetics.
        base (int): the base value
    """    
    @measure_time
    def power_test(interval: int, base: int, power: int = 4):
        for x in range(interval):
            result = base**power    

    @measure_time
    def test_multiplication_for(interval: int, base: int, power: int = 4):
        for x in range(interval):
            result = base
            for y in range(power):
                result *= base

    @measure_time
    def test_just_multiplication(interval: int, base: int):
        for x in range(interval):
            result = base * base * base * base

    power_test(interval=times, base=base)
    test_multiplication_for(interval=times, base=base)
    test_just_multiplication(interval=times, base=base)

@log_results            
def feladat_2() -> list[int, int]:
    """ (2.5) 5^4^3^2 first digits: "62060698786608744707" and last digits: "92256259918212890625" 

    Returns:
        list[int, int]: first and last digits
    """        
    mpmath.mp.dps = 20
    result_first = mpmath.power(5, 4**3**2**1)
    result_last = pow(5, 4**3**2**1, 10**20)
    return result_first, result_last

@log_results            
def feladat_3(precision_digits: int) -> float:
    """ (3.3) A Gauss-Legendre algorithm.

    Args:
        precision_digits (int): the pi digits to count.

    Returns:
        float: the calculated pi
    """    
    
    precision = math.pow(0.1, precision_digits)
    a = mpmath.mpf(1)
    b = mpmath.mpf(1/math.sqrt(2))
    t = mpmath.mpf(1/4)
    p = mpmath.mpf(1)
    
    while precision < mpmath.fabs(a - b):
        mpmath.mp.dps = precision_digits
        a1 = (a+b)/2
        b = mpmath.sqrt(a*b)
        t -= p * ((a - a1)**2)
        p *= p
        a = a1
        
    pi = ((a + b)**2)/(4*t)
    return pi

@log_results
def feladat_4(p: list[int], q: list[int]) -> list[list[int], int]:
    """ (4.5) Ruffini algorithm

    Args:
        p (_type_): polinomial
        int (_type_): binomial

    Returns:
        tuple(list[int], int): returns the quotient and the remainder.
    """    
    r = -q[0]

    rows = len(q)
    cols = len(p)
    matrix = np.zeros((rows, cols))
    
    # algoritmus   
    matrix[1, 0] = p[0] # pass the first coefficient down
    for j in range(cols - 1):
        matrix[0, j + 1] = matrix[1, j] * r # Multiply the last obtained value by r
        matrix[1, j + 1] = matrix[0, j + 1] + p[j + 1]
    
    #
    result = matrix[-1]
    quotient = result[:-1]
    remainder = result[-1]
    return quotient, remainder

@log_results
def feladat_5(interval: int) -> list[int]:
    """ (6.2) emirp search

    Args:
        interval (int, optional): the interval search.

    Returns:
        list[int]: returns with the list of emirps in the interval.
    """
    
    def is_prime(n: int) -> bool:
        """ Check if it is a prime.

        Args:
            n (int): the number

        Returns:
            bool: is number n a prime?
        """
        if n < 2:
            return False

        for i in range(2, math.ceil(math.sqrt(n)), 1):
            if n % i == 0:
                return False
        return True
    
    result = []
    def check_emirp(n: int):
        return is_prime(n) and is_prime(int(str(n)[::-1]));
    for x in range(100):
        if check_emirp(x):
            result.append(x)
    return result
 
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s', handlers=[logging.StreamHandler(), logging.FileHandler('test_results.log')])
    feladat_1(times = 1000000, base = 13)
    feladat_2()
    feladat_3(precision_digits=25)
    feladat_4(p = [2, 3, 0, -4], q = [1, 1])
    feladat_5(interval = 100)

