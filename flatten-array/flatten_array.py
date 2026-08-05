def flatten(iterable):

    flat_lst = []
    for item in iterable:
        if item == None:
            iterable.remove(item)
            continue
        if isinstance(item, list):
            flat_lst.extend(flatten(item))
        else:
            flat_lst.append(item)
        print(flat_lst)
    return flat_lst

print(flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8]))