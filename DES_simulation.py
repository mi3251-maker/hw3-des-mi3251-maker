"""
Main simulation engine.
Usage: python3 DES_Simulation.py plaintext-filename key-filename
"""

import DES
import Conversion
import sys


def before():
    if len(sys.argv) != 3:
        print("Usage: python DES_Simulation.py <plaintext-file> <key-file>")
        print("Example: python DES_Simulation.py plaintext.txt key.txt")
        return

    plaintextFile = sys.argv[1]
    keyFile = sys.argv[2]
    key = open(keyFile).readline().strip()
    plaintext = open(plaintextFile).readline().strip()
    x = Conversion.str2bits(plaintext)
    return x, key


def after(decrypted):
    recoveredText = Conversion.bits2str(decrypted)
    print("recovered Text:", recoveredText)


def main():
    x, key = before()
    y = DES.encrypt(x, key)

    print("ciphertext:", y)
    assert y == "1101001111100010001000011001111011010111100110110111111000000111"

    decrypted = DES.decrypt(y, key)
    assert decrypted == x

    after(decrypted)


if __name__ == "__main__":
    main()
