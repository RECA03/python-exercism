def slices(series, length):

    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if length==0:
        raise ValueError("slice length cannot be zero")
    if length<0:
        raise ValueError("slice length cannot be negative")
    if length>len(series):
        raise ValueError("slice length cannot be greater than series length")
    
    slice_list = []
    for i in range(len(series)):
        if i+length <= len(series):
            slice_list.append(series[i:i+length])
        else:
            break

    return slice_list