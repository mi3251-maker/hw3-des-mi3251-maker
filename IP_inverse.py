"""
Author: Put your name here
"""

FINAL_PERMUTATION = [
    [40, 8, 48, 16, 56, 24, 64, 32],
    [39, 7, 47, 15, 55, 23, 63, 31],
    [38, 6, 46, 14, 54, 22, 62, 30],
    [37, 5, 45, 13, 53, 21, 61, 29],
    [36, 4, 44, 12, 52, 20, 60, 28],
    [35, 3, 43, 11, 51, 19, 59, 27],
    [34, 2, 42, 10, 50, 18, 58, 26],
    [33, 1, 41, 9, 49, 17, 57, 25],
]


def permute(bits):
    """
    :param bits: 64 bits
    :return: 64-bits IPinverse(bits)
    """
    output = ""

    for row in range(8):
        for col in range(8):
            index = FINAL_PERMUTATION[row][col] - 1
            output += bits[index]

    return output
