def set_difference(set_one, set_two):
    result = {i for i in set_one if i not in set_two}
    return result


def set_intersection(set_one, set_two):
    result = {i for i in set_one if i in set_two}
    return result


def set_union(set_one, set_two):
    result = {i for j in (set_one, set_two) for i in j}
    return result
