# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

def match_string(text):
    pattern = r"ab*"
    
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

# Test examples
test_strings = ["a", "ab", "abb", "abbb", "b", "ba", "aa"]

for s in test_strings:
    if match_string(s):
        print(f"{s} -> Match")
    else:
        print(f"{s} -> No match")

# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

def match_string(text):
    # a - одна буква 'a'
    # b{2,3} - ровно две или три буквы 'b'
    pattern = r"ab{2,3}"
    
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

# Тестовые примеры
test_strings = ["ab", "abb", "abbb", "abbbb", "a", "abc"]

for s in test_strings:
    if match_string(s):
        print(f"{s} -> Match")
    else:
        print(f"{s} -> No match")

# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
def find_sequences(text):
    pattern=r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)
test=["a_b", "hello_world", "Python_code"]
for s in test:
    if re.fullmatch(r'[a-z]+(_[a-z]+)+', s):
        print(f"{s} -> Match")
    else:
        print(f"{s} -> No Match")

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re
def find_sequences(text):
    pattern=r'[A-Z][a-z]+'
    if re.fullmatch(pattern, text):
        return True
    else:
        return False
    
test_strings=["Abc", "Apple", "ABC", "A123"]
for s in test_strings:
    if match_string(s):
        print(f"{s} -> Match")
    else:
        print(f"{s} -> No Match")

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
def match_string(text):
    pattern=r"a.*b"
    if re.fullmatch(pattern, text):
        return True
    else:
        return False
    
text_string=["ab", "acccb", "a", "AB"]
for s in text_string:
    if match_string(s):
        print(f"{s} -> Match")
    else:
        print(f"{s} -> No Match")

# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
def special_chars(text):
    pattern=r"[ ,.]"
    result=re.sub(pattern, ":" , text)
    return result
text_string=["Hello World", "Hi, my name is Nurali", " kbtu@.kz"]
for s in text_string:
    new_s=special_chars(s)
    print(f"before:{s} -> after:{new_s}")

# Write a python program to convert snake case string to camel case string.
import re
def snake_to_camel(text):
    pattern=r"_([a-z])"
    res=re.sub(pattern, lambda match: match.group(1).upper(), text)
    return res
test_strings = ["hello_world", "snake_case_example", "my_variable_name"]
for s in test_strings:
    print(f"snake: {s:<20} Camel: {snake_to_camel(s)}")

# Write a Python program to split a string at uppercase letters.
import re
def split_string_uppercase(text):
    pattern=r"(?=[A-Z])"
    res=list(filter(None, re.split(pattern, text)))
    return res
test_string = "PythonIsGreatAndRegexIsCool"
words=split_string_uppercase(test_string)
print(f"Before: {test_string}")
print(f"After: {words}")

# Write a Python program to insert spaces between words starting with capital letters.
import re

def insert_space_smart(text):
    pattern = r"(?<=[a-z])(?=[A-Z])"
    return re.sub(pattern, " ", text)

test_strings = [
    "PythonIsGreat",
    "CamelCaseString",
    "ILoveRegex",
    "NuraliIsStudent",
    "NASAIsSpaceAgency" 
]
for s in test_strings:
    print(f"before: {s:<20} -> after: {insert_space_smart(s)}")

# Write a Python program to convert a given camel case string to snake case.
import re
def camel_to_snake(text):
    pattern=r'([A-Z])'
    snake=re.sub(pattern, r'-\1', text).lower().lstrip('_')
    return snake
test_string=["camelCase", "pythonIsGreat", "ImaStudent"]
for s in test_string:
    print(f"Camel: {s:<20} -> Snake: {camel_to_snake(s)}")