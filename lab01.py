def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    total = 1
    for i in range(k):
        total *= (n-i)
    return total


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for i in range (1, n+1):
        if i%k == 0:
            print(i)
            count+=1
    return count



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    #how big the number is
    size = len(str(y))-1
    # the value to return
    total = 0
    # run a loop till you end the digits of the number
    while size >0:
        #this will divide the number by the 10 (raised to a power) and return the number
        total += int(y/(10**(size)))
        #this will return he number after eliminating the first digit
        divider= int(y/(10**(size))) * (10**(size))
        y = y % divider
        # when the loop is at the last digit
        if size-1 ==0:
            total +=y
        #for the loop
        size-=1 
    #return the value
    return total


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    if n/100 == 0 and n == 88:
        return True
    while n / 10 !=0:
        if n % 100 == 88 and n/100 !=0:
            return True
        
        n = int(n/10)
    return False


    
