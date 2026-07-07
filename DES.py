"""
DES encryption and decryption algirithms
"""

import Key_schedule
import IP
import Rounds
import IP_inverse


def encrypt_with_subkeys(x, subkeys):
    output = IP.permute(x)
    output = Rounds.rounds(output, subkeys)
    output = IP_inverse.permute(output)
    return output


def encrypt(x, key):
    """
    DES encryption algorithm
    :param x: 64-bit plaintext
    :param key: 64-bit key
    :return: 64-bit encrypted text
    """
    subkeys = Key_schedule.generate_subkeys_encryption(key)
    return encrypt_with_subkeys(x, subkeys)


def decrypt(y, key):
    """
    DES decryption algorithm
    :param y: 64-bit ciphertextå
    :param key: 64-bit key
    :return: 64-bit decrypted text
    """
    subkeys = Key_schedule.generate_subkeys_decryption(key)
    return encrypt_with_subkeys(y, subkeys)
