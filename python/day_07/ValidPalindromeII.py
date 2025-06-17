'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

'''
'''
def valid_palindrome_one_delete(s):
    def is_palindrome_range(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Try skipping either left or right character
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        left += 1
        right -= 1
    return True

print(valid_palindrome_one_delete("racecar"))     # True → already a palindrome
print(valid_palindrome_one_delete("abca"))        # True → delete 'b' or 'c'
print(valid_palindrome_one_delete("abc"))         # False → needs >1 deletion
'''

def can_be_palindrome_with_m_modifications(s, m):
    """
    Returns True if the string s can be turned into a palindrome
    with at most m character modifications. Also prints the modifications needed.
    """
    s = list(s)  # Convert to list so it's mutable
    left, right = 0, len(s) - 1
    modifications = []

    while left < right:
        if s[left] != s[right]:
            modifications.append((left, right, s[left], s[right]))
            if len(modifications) > m:
                return False, modifications
        left += 1
        right -= 1

    return True, modifications


# Example usage
s = "abccda"
m = 1
result, changes = can_be_palindrome_with_m_modifications(s, m)

if result:
    print(f"✅ YES — Can be a palindrome with ≤ {m} modifications.")
    print("Required modifications (left_index, right_index, left_char, right_char):")
    for change in changes:
        print(change)
else:
    print(f"❌ NO — Needs more than {m} modifications ({len(changes)} needed).")
    print("Conflicting character pairs:")
    for change in changes:
        print(change)

