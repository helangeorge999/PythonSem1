# def reverse_string_recursion(s):
#     if len(s) <= 1:
#         return s
#     else:
#         return reverse_string_recursion(s[1:]) + s[0]

# # Example usage:
# original_string = "hello"
# reversed_string = reverse_string_recursion(original_string)
# print("Original string:", original_string)
# print("Reversed string:", reversed_string)



#using loop
def reverse_string_for_loop(s):
    reversed_str = ""
    for char in s[::-1]:
        reversed_str += char
    return reversed_str

# Example usage:
original_string = "hello"
reversed_string = reverse_string_for_loop(original_string)
print("Original string:", original_string)
print("Reversed string:", reversed_string)
