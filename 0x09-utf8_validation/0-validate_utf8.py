#!/usr/bin/python3
"""
Validate utf-8

"""
def validUTF8(data):
    """
        Function Valid UTF-8
    """
    for i in data:
        bin = '{0:08b}'.format(i)
        if len(bin) > 8:
            return False

    return True
