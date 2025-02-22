print("\n-------------------------task1:---------------------------\n")

import math

numbers = [1, 2, 3, 4, 5]
result = math.prod(numbers)
print("Произведение всех чисел в списке:", result)



print("\n-------------------------task2:---------------------------\n")

def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

text = "Hello World!"
upper, lower = count_upper_lower(text)
print("Заглавные буквы:", upper)
print("Строчные буквы:", lower)



print("\n-------------------------task3:---------------------------\n")

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

text = "A man a plan a canal Panama"
if is_palindrome(text):
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")



print("\n-------------------------task4:---------------------------\n")

import time
import math

def sqrt_after_delay(number, delay):
    time.sleep(delay / 1000)  # Millisekunds delay
    return math.sqrt(number)

number = 25100
delay = 2123

result = sqrt_after_delay(number, delay)
print(f"Square root of {number} after {delay} miliseconds is {result}")



print("\n-------------------------task5:---------------------------\n")

def all_elements_true(t):
    return all(t)

tuple1 = (True, True, True)
tuple2 = (True, False, True)

print("All elements of tuple1 are true:", all_elements_true(tuple1))
print("All elements of tuple2 are true:", all_elements_true(tuple2))


