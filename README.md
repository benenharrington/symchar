Symchar is a python package for generating character tables of symmetric groups.

    >>> import symchar
    >>> symchar.character_table(3)
    CharacterTable([[ 1,  1,  1],
                [-1,  0,  2],
                [ 1, -1,  1]])

There is some support for basic operations on characters, such as decomposing the tensor product.

    >>> _.tensor_product_decomposition(_[1], _[1])
    {[3]: 1, [2, 1]: 1, [1, 1, 1]: 1}

The method for constructing the character table follows Lecture 6 of G.D. James' _The Representation Theory of Symmetric Groups_. 

This was a toy project to generate data for  [link-to-ml-kronecker-coefficents]. This only required character tables up to n=15, which takes a few seconds with symchar. If you want to work with larger symmetric groups, you should probably use something like GAP. 