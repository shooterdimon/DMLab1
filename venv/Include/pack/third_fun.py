from pack import set_function as fun

set_z = ""

def result_z(set_a, set_c, set_u):
    global set_z
    set_x = fun.set_difference(set_u, set_a)
    set_y = set_c
    set_z = fun.set_union(fun.set_difference(set_x, set_y),fun.set_difference(set_y, set_x))
    return set_z
