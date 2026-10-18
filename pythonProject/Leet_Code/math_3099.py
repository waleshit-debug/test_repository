# 3099. Harshad Number
# An integer divisible by the sum of its digits is said to be a Harshad number.
# You are given an integer x.
# Return the sum of the digits of x if x is a Harshad number,
# otherwise, return -1.

x = int(input())
text_number = str(x)
init_value = 0
negative_value = -1
for f in text_number:
    init_value = init_value + int(f)

if x % init_value == 0:
    print(init_value)
else:
    print(negative_value)
