"""This is the main module"""
import random


def main() -> list[int]:
    """The main function to be called by the pipeline

    :return: _description_
    :rtype: list[int]
    """
    _list = [random.randint(0, 20) for _ in range(50)]

    return _list
