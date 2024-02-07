print("Het_Kothari_60004230270")

#Lists
my_list = [1,2,3]
my_list.append(4)
print("List after appending: ", my_list)

my_list.extend([7,8])
print("List after extending: ", my_list)

my_list.insert(1,10)
print("List after inserting: ", my_list)

#Tuples
my_tuple = (1,2,3)
print("Tuple: ", my_tuple)

#Sets
my_set = {1,2,3}
print("Set after adding: ", my_set)

my_set.remove(3)
print("Set after removing: ", my_set)

set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
print("The union of sets: ", union_set)

#Dictionaries
my_dict = {'name': 'Het', 'age': 19}
key_list = list(my_dict.keys())
print("Keys in the dictionary: ", key_list)

values_list = list(my_dict.values())
print("Values in the dictionary: ", values_list)

items_list = list(my_dict.items())
print("Key and value pairs in the dictionary are: ", items_list)
