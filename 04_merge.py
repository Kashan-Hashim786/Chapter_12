# Initializing two dictionaries with duplicate keys
dict1 = {'a': 1, 'b': 2, 'b': 17, 'b': 54}  # Note: Only the last value for 'b' will be kept (54)
dict2 = {'c': 3, 'd': 4, 'b': 5, 'b': 10, 'b': 24}  # Only the last value for 'b' will be kept (24)

# Merging the two dictionaries
# The values from dict2 will override any matching keys in dict1 (in this case, key 'b' will be from dict2)
merge = dict1 | dict2

print(merge)  # Output: {'a': 1, 'b': 24, 'c': 3, 'd': 4}
