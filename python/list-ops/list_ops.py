def append(list1, list2):
    return list1 + list2


def concat(lists):
    concatenated_list = []
    for list in lists:
        concatenated_list += list
    return concatenated_list


def filter(function, list):
    filtered_list = []
    for item in list:
        if function(item):
            filtered_list += [item]
    return filtered_list


def length(list):
    counter = 0
    for item in list:
        counter += 1
    return counter


def map(function, list):
    mapped_list = []
    for item in list:
        mapped_list += [function(item)]
    return mapped_list


def foldl(function, list, initial):
    accumulator = initial
    for indx in range(length(list)):
        accumulator = function(accumulator,list[indx])
    return accumulator


def foldr(function, list, initial):
    accumulator = initial
    for indx in range(length(list)-1,-1,-1):
        accumulator = function(accumulator,list[indx])
    return accumulator


def reverse(list):
    reversed_list = [list[indx] for indx in range(len(list)-1,-1,-1)]
    return reversed_list