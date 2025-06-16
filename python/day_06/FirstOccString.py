'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
'''
haystack = "sadbutsad"
needle = "sad"

def firstoccstr(haystack, needle):
    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):  # slide window from 0 to n-m
        if haystack[i:i+m] == needle:
            return i
    return -1


print(firstoccstr(haystack,needle))

