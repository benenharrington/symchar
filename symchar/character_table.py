import numpy as np

from .partition import size_of_conjugacy_class_in_symmetric_group

class CharacterTable(np.ndarray):
    def __new__(cls, input_array, partitions, n):
        return np.asarray(input_array).view(cls)
    
    def __init__(self, input_array, partitions, n):
        self.partitions = partitions
        self.partition_lookup = {partition: i for i, partition in enumerate(partitions)}
        self.group_number = n
        self.conjugacy_class_sizes = np.array([size_of_conjugacy_class_in_symmetric_group(partition) for partition in partitions], dtype='object')
        
    def get_character(self, partition):
        return self[self.partition_lookup[partition]]
    
    def inner_product(self, character_1, character_2):
        return np.dot(character_1*character_2, self.conjugacy_class_sizes)//factorial(self.group_number)
        
    def character_decomposition(self, character):
        return {partition: self.inner_product(character, self.get_character(partition)) for partition in self.partitions}
    
    def tensor_product_decomposition(self, character_1, character_2):
        return self.character_decomposition(character_1*character_2)
    
    def kronecker_coefficients(self, partition_1, partition_2):
        return self.tensor_product_decomposition(self.get_character(partition_1), self.get_character(partition_2))
    
    