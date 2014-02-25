
"""
Multiplicação de matrizes

            | 7   8|
    ×       | 9  10|
            |11  12|

|1  2  3|   |1*7+2*9+3*11  1*8+2*10+3*12|   | 7+18+33   8+20+36|   | 58   64|
|4  5  6|   |4*7+5*9+6*11  4*8+5*10+6*12|   |28+45+66  32+50+72|   |139  154|


Matrizes:

    >>> a = [(1, 2, 3),
    ...      (4, 5, 6)]
    >>> b = [( 7,  8),
    ...      ( 9, 10),
    ...      (11, 12)]

Dot product:

    >>> dot_product(a, 0, b, 0), dot_product(a, 0, b, 1)
    (58, 64)
    >>> dot_product(a, 1, b, 0), dot_product(a, 1, b, 1)
    (139, 154)

Multiplicação:

    >>> mult(a, b)  # doctest: +NORMALIZE_WHITESPACE
    [[58,  64],
     [139, 154]]


"""

def dot_product(a, linha, matriz_b, coluna):
    soma = 0
    for i, el_a in enumerate(a[linha]):
        soma += el_a * matriz_b[i][coluna]
    return soma


def mult(a, b):
    nova_matriz = []
    for i_lin in range(len(a)):
        nova_linha = []
        for i_col in range(len(b[0])):
            nova_linha.append(dot_product(a, i_lin, b, i_col))
        nova_matriz.append(nova_linha)
    return nova_matriz




