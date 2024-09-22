def non_decreasing(list):
    if len[list]==0 or len[list]==1:
        return "True"
    if list[-2]>list[-1]:
        return 'False'
    return non_decreasing(list[:-1])