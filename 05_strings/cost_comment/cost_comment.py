# I continue to use exercises involving Unicode characters for teaching purposes.
# In this exercise, let’s assume that each comment has a value equal to the Unicode character multiplied by 3
comment = input('Enter comment: ')
s = 0

for i in comment:
    s += ord(i)  # character set

product = s * 3  # final result

print(f"Message text: '{comment}'")
print(f'Cost message: {product} token(s)')
