def sparse_add(vector1: dict, vector2: dict) -> dict:
    """
    Adds two dictionaries of the same length that represent sparse vectors then returns their sum as a dictionary.

    :param vector1: The first sparse vector represented as a dictionary.
    :param vector2: The second sparse vector represented as a dictionary.
    :precondition: vector1 and vector2 must be dictionaries with a "length" key within the keys somewhere and the same "length" value for both.
    :postcondition: calculates the correct sum of the two sparse vectors.
    :return: The sum of the two sparse vectors as a dictionary.
    :raises ValueError: If the lengths of the two inputted vectors are not the same.
    :raises KeyError: If the "length" key is not in either of the inputted dictionaries.

    >>> sparse_add({"length": 3, 0: 1, 2: 3}, {"length": 3, 0: 4, 1: 5, 2: 6})
    {'length': 3, 0: 5, 1: 5, 2: 9}
    >>> sparse_add({0: 1, 2: 3, "length": 3}, {"length": 3, 0: 4, 1: 5, 2: 6})
    {'length': 3, 0: 5, 1: 5, 2: 9}
    """
    if vector1["length"] != vector2["length"]:
        raise ValueError("Both vectors should have the same length.")
    # either length key could be used since they are guaranteed to be the same especially because of the error above
    result = {"length": vector1["length"]}

    for key, value in vector1.items():
        if key != "length":
            result[key] = value

    for key, value in vector2.items():
        if key != "length":
            if key in result:
                result[key] += value
            else:
                result[key] = value

    # A sort of duct tape method to sort the keys with length being the first key and the rest in ascending order
    sorted_result = {"length": vector1["length"]}
    sorted_result.update({k: result[k] for k in sorted([key for key in result if key != "length"])})

    return sorted_result


def sparse_dot_product(vector1: dict, vector2: dict) -> int:
    """
    Calculates the dot product of two sparse vectors represented as dictionaries.

    :param vector1: The first sparse vector represented as a dictionary.
    :param vector2: The second sparse vector represented as a dictionary.
    :precondition: vector1 and vector2 must be dictionaries
    :postcondition: calculates the correct dot product of the two sparse vectors.
    :return: The dot product of the two sparse vectors as an integer.

    >>> sparse_dot_product({0: 1, 2: 3}, {0: 4, 1: 5, 2: 6})
    22
    >>> sparse_dot_product({0: -1, 2: -3}, {0: 4, 1: -5, 2: -6})
    14
    >>> sparse_dot_product({}, {})
    0
    """
    # very simple approach because realized that the only values that matter are the ones that are in both vectors
    # otherwise if the value is just present within one vector, it always gets multiplied by 0
    dot_product = 0
    for key in vector1:
        if key in vector2:
            dot_product += vector1[key] * vector2[key]
    return dot_product



def main():
    """
    Drives the program.
    """

if __name__ == "__main__":
    main()