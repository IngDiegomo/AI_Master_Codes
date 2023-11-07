def list_intersection(a , b):
    intersection = []
    for i in list(a):
        if (i in list(b)):
            intersection.append(i)
    return intersection

def remove_duplicates(a):
    unique_tuples = set(tuple(inner_list) for inner_list in list(a))
    return [list(unique_tuple) for unique_tuple in unique_tuples]
