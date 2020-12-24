"""
03. Lab 03
Addition and dot products of sparse vectors
Name : Min Soo (Mike) HWANG
Student Number : A01198733
Set : F
Github ID : sis00337 (Delivery_KiKi)
"""


def sparse_add(first_vector, second_vector):
    """ Calculate the sum of two sparse vectors and return the result in a dictionary format.

    :param first_vector: a dictionary corresponding to a sparse vector including length key
    :param second_vector: a dictionary corresponding to a sparse vector including length key
    :precondition: the length key in each dictionary must have the same value
                   all keys and values in dictionaries must be integers
                   the keys must be equal to or greater than 0 and less than length [0, length)
    :postcondition: correctly calculate the sum of the two sparse vectors
    :return: a dictionary corresponding to the sum of the two sparse vectors

    >>> sparse_add({0: -4, 1: 2, 2: 10, 'length': 3}, {0: 4, 1: 5, 'length': 3})
    {1: 7, 2: 10, 'length': 3}
    >>> sparse_add({0: 77, 2: 80, 4: -77, 'length': 5}, {0: 4, 2: 25, 4: 90, 'length': 5})
    {0: 81, 2: 105, 4: 13, 'length': 5}
    >>> sparse_add({4: 22, 7: 42, 'length': 10}, {0: 4, 3: 90, 7: 18, 9: -33, 'length': 10})
    {0: 4, 3: 90, 4: 22, 7: 60, 9: -33, 'length': 10}
    """
    # Initialize a dictionary
    sum_vector = {}
    # Calculate the sum of two vectors
    for key_1, value_1 in first_vector.items():
        for key_2, value_2 in second_vector.items():
            if key_1 == key_2 and key_1 not in sum_vector:
                sum_vector[key_1] = value_1 + value_2
            elif key_1 == key_2 and key_1 in sum_vector:
                sum_vector[key_1] = value_1 + value_2
            elif key_1 not in sum_vector:
                sum_vector[key_1] = value_1
            elif key_2 not in sum_vector:
                sum_vector[key_2] = value_2

    # Sort the dictionary for being good-looking
    del sum_vector['length']
    sum_vector = dict(sorted(sum_vector.items()))
    sum_vector['length'] = first_vector['length']
    # Remove the value of 0 from the dictionary
    for sum_key in list(sum_vector.keys()):
        if sum_vector[sum_key] == 0:
            del sum_vector[sum_key]

    return sum_vector


def sparse_dot_product(first_vector, second_vector):
    """ Calculate the dot product of two sparse vectors

    :param first_vector: a dictionary corresponding to a sparse vector including length key
    :param second_vector: a dictionary corresponding to a sparse vector including length key
    :precondition: the length key in each dictionary must have the same value
                   all keys and values in dictionaries must be integers
                   the keys must be equal to or greater than 0 and less than length [0, length)
    :postcondition: correctly calculate the dot product of the two sparse vectors
    :return: an integer corresponding the result of dot product between two vectors

    >>> sparse_dot_product({0: -4, 1: 2, 2: 10, 'length': 3}, {0: 4, 1: 5, 'length': 3})
    -6
    >>> sparse_dot_product({0: 4, 1: 5, 2: 25, 4: 5, 'length': 5}, {0: 5, 1: 16, 2: -4, 4: 12, 'length': 5})
    60
    >>> sparse_dot_product({4: 20, 7: 5, 'length': 10}, {0: 4, 3: 90, 7: 18, 9: -33, 'length': 10})
    90
    """
    # Initialize a dictionary
    product_vector = {}
    # Calculate the dot product of the two vectors
    for key_1, value_1 in first_vector.items():
        for key_2, value_2 in second_vector.items():
            if key_1 == key_2 and key_1 not in product_vector:
                product_vector[key_1] = value_1 * value_2
            elif key_1 == key_2 and key_1 in product_vector:
                product_vector[key_1] = value_1 * value_2
            elif key_1 not in product_vector:
                product_vector[key_1] = 0
            elif key_2 not in product_vector:
                product_vector[key_2] = 0
    # Initialize a variable
    result = 0
    # Calculate the sum of each product
    for product_key in list(product_vector.keys()):
        if product_key != 'length':
            result += product_vector[product_key]
    return result


def main():
    # Program starts here

    import doctest
    doctest.testmod(verbose=True)

    # first_vector = {0: -4, 1: 2, 2: 10, 'length': 3}
    # second_vector = {0: 4, 1: 5, 'length': 3}
    # test_add = sparse_add(first_vector, second_vector)
    # print(test_add)
    # test_dot_product = sparse_dot_product(first_vector, second_vector)
    # print(test_dot_product)


if __name__ == "__main__":
    # Invoke the main function
    main()
