
"""
Multiplicação de matrizes


Em preparação para paralelizar, esta versão de dotproduct modifica a matrizes
resultado in-place

            | 7   8|
    ×       | 9  10|
            |11  12|

|1  2  3|   |1*7+2*9+3*11  1*8+2*10+3*12|   | 7+18+33   8+20+36|   | 58   64|
|4  5  6|   |4*7+5*9+6*11  4*8+5*10+6*12|   |28+45+66  32+50+72|   |139  154|


Matrizes:

    >>> matriz(3, 2)
    [[0, 0], [0, 0], [0, 0]]
    >>> a = [(1, 2, 3),
    ...      (4, 5, 6)]
    >>> b = [( 7,  8),
    ...      ( 9, 10),
    ...      (11, 12)]

Dot product:

    >>> resultado = matriz(2, 2)
    >>> dot_product(resultado, a, 0, b, 0)
    >>> dot_product(resultado, a, 0, b, 1)
    >>> dot_product(resultado, a, 1, b, 0)
    >>> dot_product(resultado, a, 1, b, 1)
    >>> resultado  # doctest: +NORMALIZE_WHITESPACE
    [[58,  64],
     [139, 154]]

Multiplicação:

    >>> mult(a, b)  # doctest: +NORMALIZE_WHITESPACE
    [[58,  64],
     [139, 154]]


"""

import threading
import time
import sys

def matriz(linhas, colunas):
    return [[0]*colunas for i in range(linhas)]


def dot_product(res, a, linha, b, coluna):
    soma = 0
    for i, el_a in enumerate(a[linha]):
        soma += el_a * b[i][coluna]
    res[linha][coluna] = soma
    time.sleep(5)


def mult(a, b):
    nova_matriz = matriz(len(a), len(b[0]))
    for i_lin in range(len(a)):
        for i_col in range(len(b[0])):
            thread = threading.Thread(target=dot_product, args=(nova_matriz, a, i_lin, b, i_col))
            thread.start()

    while threading.active_count() > 1:
        print('.', end=' ')
        sys.stdout.flush()
        time.sleep(0.1)

    return nova_matriz

if __name__=='__main__':
    a = [(1, 2, 3),
         (4, 5, 6)]
    b = [( 7,  8),
         ( 9, 10),
         (11, 12)]
    print(mult(a, b))
