def list_intersection(a:list , b:list):
    intersection = []
    for i in a:
        if (i in b):
            intersection.append(i)
    return intersection

def remove_duplicates(a:list):
    unique_tuples = set(tuple(inner_list) for inner_list in a)
    return [list(unique_tuple) for unique_tuple in unique_tuples]
