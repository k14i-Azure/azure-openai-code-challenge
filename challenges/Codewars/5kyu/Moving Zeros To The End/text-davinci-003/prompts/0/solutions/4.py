def move_zeros(lst):
    if not lst:
        return lst
    zeros = [x for x in lst if x == 0]
    non_zeros = [x for x in lst if x != 0]
    return non_zeros + zeros
