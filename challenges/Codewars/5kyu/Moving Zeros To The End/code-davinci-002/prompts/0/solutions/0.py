def move_zeros(lst):
    zeros = []
    for i in range(len(lst)):
        if lst[i] == 0:
            zeros.append(lst.pop(i))
            i -= 1
    return lst + zeros

"""
/*
Good luck!
*/
"""
