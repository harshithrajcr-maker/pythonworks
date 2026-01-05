
"""
set

define :st ={10,20}  unorderd(indexing not supported) mutable duplicates not allowded
        st=set() ->empty set

class set :

    def union(set_obj)

    def intersection(set_obj)

    def difference(set_obj)

    def is_superset()

    def is_subset()
"""

# numbers = {100,200,300,400,300}

# print(numbers)

set_a ={100,200,300,400}

set_b = {10,20,30,300,400,40}

print(set_a.issuperset(set_b))

print(set_b.issuperset(set_a))


# union_set = set_a.union(set_b)#{100,200,300,400,10,20,30,40}

# print(union_set)

# intersection_set = set_a.intersection(set_b)#(300,400)

# print(intersection_set)

# difference_set = set_a.difference(set_b)

# print(difference_set)


