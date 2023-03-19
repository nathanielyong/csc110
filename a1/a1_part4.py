"""CSC110 Fall 2021 Assignment 1, Part 4

Instructions (READ THIS FIRST!)
===============================

Please follow the instructions in the assignment handout to complete this file.
"""
import random

import a1_image


def maximize_channels(old_pixel: tuple, value: int) -> tuple:
    """Return a new pixel that has colour channels set to the larger of value or the corresponding
    colour channel in old_pixel.

    >>> example_pixel = (100, 12, 155)
    >>> maximize_channels(example_pixel, 128)
    (128, 128, 155)
    """
    r = max(old_pixel[0], value)
    g = max(old_pixel[1], value)
    b = max(old_pixel[2], value)
    return (r, g, b)


def divide_channels(old_pixel: tuple, denominator: int) -> tuple:
    """Return a new pixel that has colour channels set to the quotient from dividing the
    corresponding colour channel in old_pixel by denominator.

    >>> example_pixel = (100, 12, 155)
    >>> divide_channels(example_pixel, 2)
    (50, 6, 77)
    """
    r = old_pixel[0] // denominator
    g = old_pixel[1] // denominator
    b = old_pixel[2] // denominator
    return (r, g, b)


def add_pepper(pixel_data: list, k: int) -> list:
    """Return a new list of pixels formed from the corresponding pixels in pixel_data that has some
    randomly chosen black pixels.

    The chance that a new pixel will be black is based on k. The probability that a pixel is
    black is to be : 1 / (k + 1)

    Assume that k >= 0.

    You must use the divide_channels function (above).

    Hint: use the function random.choice to choose from a list of denominators. What denominator,
    passed to divide_channels, causes a pixel to not change its colour? What denominator causes a
    pixel to become black?

    Because of the randomness, we can't specify an exact doctest.
    """
    denominators = [1 for _ in range(k)] + [256]
    return [divide_channels(pixel, random.choice(denominators)) for pixel in pixel_data]


def add_salt(pixel_data: list, k: int) -> list:
    """Return a new list of pixels formed from the corresponding pixels in pixel_data that has some
    randomly chosen white pixels.

    The chance that a new pixel will be white is based on k. The probability that a pixel is
    white is to be : 1 / (k + 1)

    Assume that k >= 0.

    You must use the maximize_channels function (above).

    Hint: use the function random.choice to choose from a list of values. What value, passed to
    maximize_channels, causes a pixel to not change its colour? What value causes a pixel to become
    white?

    Because of the randomness, we can't specify an exact doctest.
    """
    values = [1 for _ in range(k)] + [255]
    return [maximize_channels(pixel, random.choice(values)) for pixel in pixel_data]


def add_salt_and_pepper(pixel_data: list, k: int) -> list:
    """Return a new list of pixels formed from the corresponding pixels in pixel_data
    that has some randomly chosen white pixels and some randomly chosen black pixels.

    You must use the add_pepper then add_salt functions, in that order, with both using noise
    probabilities determined by k.

    Because of the randomness, we can't specify an exact doctest.
    """
    pepper = add_pepper(pixel_data, k)
    return add_salt(pepper, k)


def run_salt_and_pepper_example(source: str, destination: str, k: int) -> None:
    """Add salt and pepper noise to an example image file at source and save the result in
    destination, where noisiness is a function of k.

    You can run this function with an image of your choice. Make sure the image is not too large or
    this will take a long time.
    """
    original_pixel_data, width, height = a1_image.load_image(source)
    noisy_pixel_data = add_salt_and_pepper(original_pixel_data, k)
    a1_image.save_image(destination, noisy_pixel_data, width, height)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['random', 'a1_image'],
    #     'max-line-length': 100
    # })
