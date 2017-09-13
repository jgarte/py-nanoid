from os import urandom
import math

def nanoid(alphabet='_~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', size=22):
    """
    Create a nanoid with prefilled defaults
    :param alphabet:
    :param size:
    :return:
    """
    return format(alphabet, size)

def format(alphabet, size):
    """
    Create a random id from alphabet and size
    :param alphabet:
    :param size:
    :return:
    """
    masks = [15, 31, 63, 127, 255]
    mask = None
    for m in masks:
        if m >= len(alphabet) - 1:
            mask = m
            break
    step = math.ceil(1.6*mask*size/len(alphabet))
    id = ""
    while True:
        random_bytes = urandom(step)
        for i in range(step):
            byte = random_bytes[i] & mask
            if alphabet[byte]:
                id += alphabet[byte]
                if len(id) == size:
                    return id


if __name__ == "__main__":
    print(nanoid(size=3))
