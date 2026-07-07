"""
FeistelNetwork consists of 16 rounds.
Each round performs identical operations.
Author: Put your name here
"""

EXPANSION = [
    [32, 1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8, 9],
    [8, 9, 10, 11, 12, 13],
    [12, 13, 14, 15, 16, 17],
    [16, 17, 18, 19, 20, 21],
    [20, 21, 22, 23, 24, 25],
    [24, 25, 26, 27, 28, 29],
    [28, 29, 30, 31, 32, 1],
]

S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ],
]

PERMUTATION = [
    [16, 7, 20, 21, 29, 12, 28, 17],
    [1, 15, 23, 26, 5, 18, 31, 10],
    [2, 8, 24, 14, 32, 27, 3, 9],
    [19, 13, 30, 6, 22, 11, 4, 25],
]


def rounds(input, subkeys):
    """
    16 rounds of DES encryption
    :param input: 64-bit string output of IP
    :param subkeys: an array of 16 subkeys
    :return: a 64-bit string that will be fed into the final IP.
    """
    l = input[:32]
    r = input[32:]

    for round in range(16):
        old_r = r
        f_output = F_function(r, subkeys[round])
        new_r = ""
        for i in range(32):
            new_r += str(int(l[i]) ^ int(f_output[i]))
        l = old_r
        r = new_r

    return r + l


def F_function(r, subkey):
    """
    The F function used in each round
    Step 1 : expansion
    Step 2 : xor
    Step 3 : substitution
    Step 4 : permutation
    :param r: - 32-bit right half of the input used for this round
    :param key: - 48-bit subkey used for this round
    :return: a 32-bit string
    """
    expanded = expand(r)
    xored = xor(expanded, subkey)
    substituted = substitute(xored)
    permuted = permute(substituted)

    return permuted


def expand(r):
    """
    Step 1 in the F function
    Expand 32-bit input to 48-bit result using the expansion substitution table
    :param r: a 32-bit string
    :return: a 48-bit string
    """
    output = ""

    for row in range(8):
        for col in range(6):
            index = EXPANSION[row][col] - 1
            output += r[index]

    return output


def xor(input1, input2):
    """
    Step 2 in the F function
    A subkey is added to a round
    :param input1: - output of Expansion
    :param input2: - subkey
    :return: input1 xor input2
    """
    output = ""

    for i in range(len(input1)):
        bit1 = int(input1[i])
        bit2 = int(input2[i])
        output += str(bit1 ^ bit2)

    return output


def substitute(input):
    """
    Step 3 in the F funciton.
    Divide the 48-bit input into 8 6-bit blocks each of which is substitued by
    a different S-box
    :param input: 48 output bits of Step 2
    :return: a 32-bit combined outputs of the S-boxes
    """
    output = ""

    for i in range(8):
        block = input[i * 6 : (i + 1) * 6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        value = S_BOXES[i][row][col]
        output += format(value, "04b")

    return output


def permute(input):
    """
    Step 4 in the F funciton
    Permutes 32-bit input using the P permutation table
    :param input: - 32-bit string to feed into the P permutation table
    :return: a 32-bit output of the F function
    """
    output = ""

    for row in range(4):
        for col in range(8):
            index = PERMUTATION[row][col] - 1
            output += input[index]

    return output
