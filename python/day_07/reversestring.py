'''
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''
s = ["h","e","l","l","o"]
#def revstr(s):
    #return s[::-1]

def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]  # Swap characters
        left += 1
        right -= 1
    return


s = ["h", "e", "l", "l", "o"]
reverseString(s)     # modifies s in-place
print(s)             # now s is ['o', 'l', 'l', 'e', 'h']
