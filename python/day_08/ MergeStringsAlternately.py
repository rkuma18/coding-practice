'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

'''
word1 = 'abc'
word2 = 'pqr'

mergeword = ''
min_len = min(len(word1), len(word2))

for i in range(min_len):
    mergeword += word1[i] + word2[i]

print(mergeword)

word1 = 'abc'
word2 = 'pqr'

i = 0  # pointer for word1
j = 0  # pointer for word2

mergeword = ''

# Loop while both pointers are within their respective words
while i < len(word1) or j < len(word2):
    if i < len(word1):
        mergeword += word1[i]
        i += 1
    if j < len(word2):
        mergeword += word2[j]
        j += 1

print(mergeword)
