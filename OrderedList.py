def inOrder(lst):
    ret = True
    if len(lst) > 1:
        for i in range (1, len(lst)):
            ret = lst[i] >= lst[i-1] and ret
    return ret