import math
import random

"""Developer: Owen O. Phakade""
""""This is my implementation of an asymmetric crytographic algorithm called RSA. based on Modular arithmatic (Eucleadian Algorithm & Extended EA) """
""" This module has four function: 
        choose_e( takes totient of n as an argument ) -> randomly chooses a prime when combined with the totient the gcd is 1.
        generate_keys() -> generates a public and private key pair. """


def choose_e(totient):
    list_primes = []
    for e in range(2, totient):
        if math.gcd(e, totient) == 1:
            list_primes.append(e)
    return random.choice(list_primes)


def generate_keys():
    # select two prime numbers
    p = 29
    q = 23
    # compute the modulus
    n = p*q
    # compute the totient of n
    T = (p-1)*(q-1)
    # choose e //public key
    e = choose_e(T)
    # compute the private key
    d = 0
    for k in range(1, e):
        if ((1+k*T)/e).is_integer():
            d = k
            break
    return e, d, n
