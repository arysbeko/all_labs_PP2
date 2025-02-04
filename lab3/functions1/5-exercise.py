from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

print(string_permutations("abc"))  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']