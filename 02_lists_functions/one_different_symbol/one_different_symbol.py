#    Conditions:
# 1. The word are the same length
# 2. Only one character differs in each word

def is_one_away(word1, word2):
    count = 0
    if len(word1) == len(word2):  # the first condition is checked
        for i in range(len(word1)):
            if word1[i] != word2[i]:  # the second condition id checked
                count += 1
    if count == 1:  # if the difference is only one letter, the result is True
        return True
    return False


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))
