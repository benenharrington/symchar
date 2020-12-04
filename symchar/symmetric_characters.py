import numpy as np

from .character_table import CharacterTable
from .partition import generate_partitions
from .utils import coefficient_of_A, construct_B

def character_table(n):
    """
    Takes as input a positive integer n, returns the character table of the symmetric 
    group on n letters. The rows and columns of the character table are ordered by the dominance 
    order on the corresponding partitions.
    """
    partitions = [partition for partition in generate_partitions(n)]
    A = np.array([[coefficient_of_A(mu, nu) for nu in partitions] for mu in partitions], dtype='object')
    B = construct_B(A, n, partitions)
    raw_table = np.round(np.dot(B, np.linalg.inv(np.transpose(A.astype(float)))).astype(float)).astype(int).astype('object')
    return CharacterTable(raw_table, partitions, n)