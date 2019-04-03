from pack import set_function as fun

operation_1 = ""
operation_2 = ""
operation_3 = ""
operation_4 = ""
operation_5 = ""
operation_6 = ""
operation_7 = ""



def long_result(set_a, set_b, set_c, set_u):
    global operation_1, operation_2, operation_3, operation_4, operation_5, operation_6, operation_7
    operation_1 = fun.set_difference(set_u, set_a)
    operation_2 = fun.set_difference(set_u, set_b)
    operation_3 = fun.set_union(operation_1, operation_2)
    operation_4 = fun.set_difference(set_u, set_c)
    operation_5 = fun.set_union(operation_2, operation_4)
    operation_6 = fun.set_intersection(operation_3, operation_5)
    operation_7 = fun.set_difference(set_u, operation_6)
    return operation_7


