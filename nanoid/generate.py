# coding: utf-8

from itertools import islice
from math import ceil, log
from os import urandom

from nanoid import resources


def generate(alphabet=resources.alphabet, size=resources.size):
    alphabet_len = len(alphabet)

    mask = 2
    if alphabet_len > 1:
        mask = (2 << int(log(alphabet_len - 1) / log(2))) - 1
    step = int(ceil(1.6 * mask * size / alphabet_len))

    random_bytes = bytearray(urandom(step))

    filtered = (
        alphabet[random_bytes[i] & mask]
        for i in range(step)
        if random_bytes[i] & mask < alphabet_len
    )

    return ''.join(islice(filtered, size))


if __name__ == '__main__':
    print(generate())
