from functools import reduce
from math import factorial, sqrt
import numpy as np

from .character_table import CharacterTable
from .partition import Partition, generate_partitions, size_of_conjugacy_class_in_symmetric_group

def contribution_from_cover(cover):
    return reduce(lambda x, y: x*y, [size_of_conjugacy_class_in_symmetric_group(value) for value in cover.values()])

def get_partition_covers(mu, nu):
    """
    A cover of mu by nu is a function f from the set of rows of mu to the power set
    of the set of rows of nu such that the elements of each f(mu_i) sum to mu_i and 
    the disjoint union of the f(mu_i) make up nu.
    """
    if not mu:
        return [{}]
    mu_row_one = mu[0]
    reduced_mu = mu.delete_first_row()
    row_partitions = [row_partition for row_partition in generate_partitions(mu_row_one) if nu.contains(row_partition)]
    return [dictionary for dictionary_list in 
            [list_join({1: row_partition}, get_partition_covers(reduced_mu, nu.subtract(row_partition))) for 
             row_partition in row_partitions] for dictionary in dictionary_list]

def list_join(dictionary, list_of_dictionaries):
    if list_of_dictionaries == []:
        return []
    if list_of_dictionaries == [{}]:
        return [dictionary]
    return [join(dictionary, list_member) for list_member in list_of_dictionaries]

def join(dictionary_1, dictionary_2):
    return {**dictionary_1, **{key+1: value for key, value in dictionary_2.items()}}

def coefficient_of_A(mu, nu):
    return sum([contribution_from_cover(cover) for cover in get_partition_covers(mu, nu)])

def construct_B(A, n, partitions):
    B = np.zeros(A.shape, dtype='object')
    conjugacy_class_multiplier = np.array([factorial(n)//size_of_conjugacy_class_in_symmetric_group(partition) for partition in partitions], dtype='object')
    for i, mu in enumerate(partitions):
        for j, nu in enumerate(partitions[i:]):
            if j == 0:
                B[i, i] = round(sqrt(np.dot(A[i,:]**2, conjugacy_class_multiplier) - np.dot(B[:,i],B[:,i])))
            else:
                B[i, j+i] = (np.dot(A[i,:]*A[i+j,:], conjugacy_class_multiplier) - np.dot(B[:,i],B[:,i+j]))//B[i, i]
    return B
