#!/usr/bin/python3
"""
    Valited utf-8
"""


def validUTF8(data):
    """
     Function Valid UTF-8 with Bits
    """
    countBytes = 0
    oneVer = 1 << 7
    secondVer = 1 << 6

    for i in data:
        mask_n_byte = 1 << 7
        if countBytes == 0:
            while mask_n_byte & i:
                countBytes += 1
                mask_n_byte = mask_n_byte >> 1
            if countBytes == 0:
                continue
            if countBytes == 1 or countBytes > 4:
                return False
        else:
            if not (i & oneVer and not (i & secondVer)):
                return False
        countBytes -= 1
    if countBytes == 0:
        return True
    return False
