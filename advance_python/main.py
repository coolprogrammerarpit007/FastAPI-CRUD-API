#  Lists in python are ordered,mutable and allowed duplicate elements
# Tuples are ordered,Immutable and allows duplicate elements.
# Dictionary:- Key-value pair,unordered,mutable
# Sets:- are un-ordered,mutable and not allow duplicates.
# strings:- ordered and im-mutable text representation of data
# collections in python:- Counter,namedtuple,OrderDict,defaultdict,deque

from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque
#  Counter collection store item as key and their count as value

#  Counter Collection in Python
text = "aaaabbbbbcccc"
my_counter = Counter(text)
# print(my_counter)
# print(my_counter.most_common(1)) # will print most common 


# namedtuple in Python

Point = namedtuple("Point","x,y")
point1 = Point(25,50)
# print(point1)


# OrderedDict in collections
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
ordered_dict["e"] = 5

# print(ordered_dict)

#  defaultdict are like orderedDict but with have a default values
# d =  defaultdict(int)
# d['a'] = 1
# d['b'] = 2

# print(d)

d = deque()
d.append(1)
d.append(2)
# print(d)


#  Itertools in python
# itertools:- product,permutations,combinations,accumulate,groupby,and infinite operators
# print("Itertools in python")


from itertools import product,permutations,combinations,accumulate

a = [1,2,3]
b = [3,4]

prod = list(product(a,b)) # will give cartesian cross product of matrix
# print(prod)

perm = permutations(a) # will give all possible combinations
comb = combinations(a) # will give all possible combinations
# print(list(perm))