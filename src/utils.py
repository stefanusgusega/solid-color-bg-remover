"""
Module for the remover utility functions
"""
HEX_LIST = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
]


def hex_to_int(hexa: str):
    """
    Convert 2-digit hexadecimal into tuple of values.
    """
    assert len(hexa) == 2, "Len of hexadecimal should be only 2."
    return 16 * HEX_LIST.index(hexa[0]) + HEX_LIST.index(hexa[1])


def color_hex_to_int(hexa: str):
    """
    Convert color hex to tuple that consists of 3 integers
    representing red, green, and blue value
    """
    assert hexa[0] == "#", "Please begin with #"
    hexa = hexa.lower()[1:]
    return (hex_to_int(hexa[0:2]), hex_to_int(hexa[2:4]), hex_to_int(hexa[4:6]))
