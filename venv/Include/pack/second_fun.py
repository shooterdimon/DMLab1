from pack import set_function as fun

operation_1 = ""
operation_2 = ""


def short_result(set_a, set_b, set_c, set_u):
    global operation_1, operation_2, operation_3
    operation_1 = fun.set_union(set_a, set_c)
    operation_2 = fun.set_intersection(operation_1, set_b)
    return operation_2
