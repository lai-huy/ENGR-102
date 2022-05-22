# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
#               BRANDON A WHITE     331004571
#               WILLIAM A ROBERTS   530008478
#               JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 6a Activity 2
# Date:         04 October 2021
#

p = "{:d} is prime"
c = "{:d} is not prime"
out = "There are {:d} prime numbers between 2 and 100"


def is_prime(n: int) -> bool:
    """
    Determine if a number is prime.

    :param n: number to check for primality
    :return: is number is prime
    """
    # 2 and 3 are prime
    if n <= 3:
        return n > 1

    # First Prime number
    if n % 2 == 0:
        return False

    # Second Prime number
    if n % 3 == 0:
        return False

    # Since perfect squares are not prime, we only have to check up to the sqrt of n
    #
    # All prime numbers greater than 3 are in the form 6k + i or 6k - i,
    # where i = [0, 1, 2, 3, 4, 5] and k is a positive integer
    #
    # 2 removes i = [0, 2, 4]
    # 3 removes i = [3]
    # this leaves i = [1, 5]
    i = 5

    # Loop until sqrt of n
    # sqrt function is slow so we square i instead
    while i ** 2 <= n:
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
        i += 6
    return True


# Number of Primes
count = 0

# Main loop
for j in range(2, 101):
    if is_prime(j):
        count += 1
        print(p.format(j))
    else:
        print(c.format(j))

print()
print(out.format(count))
