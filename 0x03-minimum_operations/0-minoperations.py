#!/usr/bin/python3
""" Inizializate """


def minOperations(n):
    """
        0. Minimum Operations
    """
    if (not isinstance(n, int)):
        return 0

    op = 2
    mov = 0

    while (op <= n):
        if (n % op == 0):
            mov += op
            n = n // op
        else:
            op += 1

    return mov
