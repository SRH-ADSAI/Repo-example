"""This is the main module"""
import random


def main() -> list[int]:
    """_summary_

    :return: _description_
    :rtype: list[int]
    """
    _list = [random.randint(0, 20) for _ in range(50)]

    return _list
