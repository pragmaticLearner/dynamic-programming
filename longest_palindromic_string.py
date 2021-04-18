# find longest palindrome

'''
Psuedo code for implemented algorithm:

empty_array = []
for letter in string:
    letter.append(empty_array)                      *recursive function to find combinations?*
    return all combinations in empty_array

palindromes = []
if combination in empty_array is palindrome:
    palindromes.append(combination)
else:
    pass

return palindromes.max()

'''

from itertools import combinations as c


# Test for first part of algorithm
def longest_palindrome(x):
    return [''.join(l) for i in range(len(x)) for l in c(x, i + 1)]


print(longest_palindrome('abc'))
