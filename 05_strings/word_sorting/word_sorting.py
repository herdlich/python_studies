# The script returns the words in lexicographical order

s1, s2, s3 = (input('Type a word: ') for _ in range(3))

maximum, minimum = max(s1, s2, s3), min(s1, s2, s3)
medium_min_1, medium_min_2, medium_min_3 = min(s1, s2), min(s2, s3), min(s1, s3)
final_medium = max(medium_min_1, medium_min_2, medium_min_3)

print(minimum, final_medium, maximum)
