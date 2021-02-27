import math
import random

"""Developer: Owen O. Phakade"""
# """"This is my implementation of an asymmetric crytographic algorithm called RSA. based on Modular arithmatic (Eucleadian Algorithm & Extended EA) """
# """ This module has four function:
#         choose_e( takes totient of n as an argument ) -> randomly chooses a prime when combined with the totient the gcd is 1.
#         generate_keys() -> generates a public and private key pair. """


def choose_e(totient):
    list_primes = []
    for e in range(2, totient):
        if math.gcd(e, totient) == 1:
            list_primes.append(e)
    return random.choice(list_primes)


def generate_keys():
    # select two prime numbers
    p = 11
    q = 17
    # compute the modulus
    n = p*q
    # compute the totient of n
    T = (p-1)*(q-1)
    # choose e //public key
    e = choose_e(T)
    # compute the private key
    k = 0
    d = 0
    while True:
        k = k + 1
        d = (1+k*T)/e
        if d.is_integer():
            break

    return e, d, n


def encrypt(m, e, n):
    # this function takes in a message
    # from the sender and encrypts it
    # using the public key and returns
    # cipher text
    return m**e % n


def decrypt(c, d, n):
    # This function takes in a cipher text
    # from the sender and dencrypts it
    # using the private key and returns
    # the original text
    return c**int(d) % n


if __name__ == '__main__':

    e, d, modulus = generate_keys()
    message = 90
    print("--------------------------------")
    print(f'keys: e:{e}  d:{d}  n:{modulus}')
    print("--------------------------------")
    cipher_text = encrypt(message, e, modulus)
    print(f'cipher text: {cipher_text}')
    decrypted_msg = decrypt(cipher_text, d, modulus)
    print(f'send Text: {decrypted_msg}')
