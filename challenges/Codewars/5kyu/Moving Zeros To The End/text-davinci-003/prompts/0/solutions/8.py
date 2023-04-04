def move_zeros(lst):
    if not lst:
        return lst
    zeros = [i for i in lst if i == 0]
    non_zeros = [i for i in lst if i != 0]
    return non_zeros + zeros
