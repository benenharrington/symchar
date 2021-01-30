Symchar is a python package for generating character tables of symmetric groups.

    >>> import symchar
    >>> c = symchar.character_table(3)
    >>> c
    CharacterTable([[ 1,  1,  1],
                [-1,  0,  2],
                [ 1, -1,  1]], dtype=object)

There is some support for basic operations on characters, such as decomposing the tensor product.

    >>> c.tensor_product_decomposition(c[1], c[1])
    {[3]: 1, [2, 1]: 1, [1, 1, 1]: 1}

The rows and columns of the character table of S_n are indexed by the partitions of n with respect to the dominance order, but you can also look up characters by passing a Partition object:

    from symchar import Partition
    >>> mu = Partition([2, 1])
    >>> c.get_character(mu)
    CharacterTable([-1, 0, 2], dtype=object)

The method for constructing the character table follows Lecture 6 of G.D. James' _The Representation Theory of Symmetric Groups_. 

This was a toy project to generate data for [a toy project on predicting kronecker coefficients](https://github.com/benenharrington/transformer-kronecker-coefficients). This only required character tables up to n=15, which takes a few seconds with symchar. If you want to work with larger symmetric groups, you should probably use something like GAP. 
