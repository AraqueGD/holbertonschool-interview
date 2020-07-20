#!/usr/bin/python3

""" Lockboxes Interview """


def canUnlockAll(boxes):

    keys = {0: True}

    if (len(boxes) == 0):
        return False
    elif (len(boxes[0]) == 0):
        return False

    while (True):

        len_keys = len(keys)
        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < len(boxes):
                        keys[j] = True
                    boxes[i] = None

        if not(len(keys) > len_keys):
            break

    if (len_keys == len(boxes)):
        return True
    else:
        return False
