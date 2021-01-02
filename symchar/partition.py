from functools import reduce
from math import factorial

class Partition(list):
    def __init__(self, partition_list):
        super().__init__(partition_list)
        self.length = sum(self)
        self.height = len(self)
        
    def __hash__(self):
        return hash(str(self))

    def to_row_count_dictionary(self):
        return {i:self.count(i) for i in reversed(range(self.length + 1))}
    
    def pad(self, group_number):
        return Partition(self + (group_number - self.length*[1]))
    
    def subtract(self, partition):
        new_list = list(self)
        for row in partition:
            new_list.remove(row)
        return Partition(new_list)
        
    def contains(self, partition):
        new_list = list(self)
        try:
            for row in partition:
                new_list.remove(row)
        except ValueError:
            return False
        return True
    
    def delete_first_row(self):
        return Partition(self[1:])


def next_partition(partition):
    """
    Returns the partition after the input partition with respect
    to the dictionary ordering. Returns None if the input partition is minimal
    """
    if partition[0] == 1:
        return None
    i = partition.height - 1
    
    while partition[i] == 1:
        i = i - 1
        
    remove_from_row = i
    new_row_value = partition[remove_from_row] - 1
    new_partition = (partition[:remove_from_row] + [new_row_value] + 
                     complete_partition_maximally(new_row_value, partition.length - sum(partition[:remove_from_row]) - new_row_value))
    return Partition(new_partition)

def complete_partition_maximally(max_first_row, length):
    return [max_first_row]*(length // max_first_row) + [length % max_first_row] if length % max_first_row != 0 else [max_first_row]*(length // max_first_row)

def generate_partitions(n):
    partition = Partition([n])
    while partition:
        yield partition
        partition = next_partition(partition)

def size_of_conjugacy_class_in_symmetric_group(cycle_type):
    """
    If the given cycle type pads to a partition of n with a_j parts of length j,
    then the size of the conjugacy class is n! / \prod j^a_j * (a_j)!
    """
    partition = Partition(cycle_type)
    return (factorial(partition.length) // 
            reduce(lambda x, y: x*y, 
            [key**value * factorial(value) for key, value in partition.to_row_count_dictionary().items()])) 
