def move_zeros(lst):
    if not lst:
        return lst
    return [x for x in lst if x != 0] + [x for x in lst if x == 0]
