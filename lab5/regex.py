# 1. String with 'a' followed by zero or more 'b's
import re

def match_a_zero_or_more_b(text):
    pattern = r'ab*'
    return bool(re.match(pattern, text))


print("1. String with 'a' followed by zero or more 'b's:")
print(match_a_zero_or_more_b("ac"))  # True
print(match_a_zero_or_more_b("abc"))  # True
print(match_a_zero_or_more_b("a"))    # True
print(match_a_zero_or_more_b("abb"))  # True
print(match_a_zero_or_more_b("b"))    # False
print("-" * 60)

#---------------------------------------------------------------
# 2. String with 'a' followed by two to three 'b's
import re

def match_a_two_to_three_b(text):
    pattern = r'ab{2,3}'
    return bool(re.match(pattern, text))


print("2. String with 'a' followed by two to three 'b's:")
print(match_a_two_to_three_b("abb"))  # True
print(match_a_two_to_three_b("abbb")) # True
print(match_a_two_to_three_b("ab"))   # False
print(match_a_two_to_three_b("abbbb"))# False
print("-" * 60)

#---------------------------------------------------------------
# 3. Sequences of lowercase letters joined with an underscore
import re

def find_lowercase_sequences_with_underscore(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)


print("3. Sequences of lowercase letters joined with an underscore:")
print(find_lowercase_sequences_with_underscore("hello_world and_another_example"))  # ['hello_world', 'and_another']
print("-" * 60)

#---------------------------------------------------------------
# 4. Sequences of one uppercase letter followed by lowercase letters
import re

def find_uppercase_followed_by_lowercase(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)


print("4. Sequences of one uppercase letter followed by lowercase letters:")
print(find_uppercase_followed_by_lowercase("Hello World Python"))  # ['Hello', 'World', 'Python']
print("-" * 60)

#---------------------------------------------------------------
# 5. String with 'a' followed by anything, ending in 'b'
import re

def match_a_anything_b(text):
    pattern = r'a.*b$'
    return bool(re.match(pattern, text))


print("5. String with 'a' followed by anything, ending in 'b':")
print(match_a_anything_b("acb"))  # True
print(match_a_anything_b("a123b"))# True
print(match_a_anything_b("ab"))   # True
print(match_a_anything_b("ac"))   # False
print("-" * 60)

#---------------------------------------------------------------
# 6. Replace all occurrences of space, comma, or dot with a colon
import re

def replace_spaces_commas_dots_with_colon(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)


print("6. Replace all occurrences of space, comma, or dot with a colon:")
print(replace_spaces_commas_dots_with_colon("Hello, world. This is a test."))  # Hello::world::This:is:a:test:
print("-" * 60)

#---------------------------------------------------------------
# 7. Convert snake_case string to camelCase
import re

def snake_to_camel(text):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)


print("7. Convert snake_case string to camelCase:")
print(snake_to_camel("hello_world_python"))  # helloWorldPython
print("-" * 60)

#---------------------------------------------------------------
# 8. Split a string at uppercase letters
import re

def split_at_uppercase(text):
    return re.sub(r'([A-Z])', r' \1', text).strip()


print("8. Split a string at uppercase letters:")
print(split_at_uppercase("HelloWorldPython"))  # Hello World Python
print("-" * 60)

#---------------------------------------------------------------
# 9. Insert spaces between words starting with capital letters
import re

def insert_spaces_between_capital_words(text):
    return re.sub(r'(?<!^)([A-Z])', r' \1', text)


print("9. Insert spaces between words starting with capital letters:")
print(insert_spaces_between_capital_words("HelloWorldPython"))  # Hello World Python
print("-" * 60)

#---------------------------------------------------------------
# 10. Convert a given camelCase string to snake_case
import re

def camel_to_snake(text):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower()


print("10. Convert a given camelCase string to snake_case:")
print(camel_to_snake("helloWorldPython"))  # hello_world_python
print("-" * 60)