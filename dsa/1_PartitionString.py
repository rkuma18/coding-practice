'''
Given a string s, partition it into unique segments according to the following procedure:

Start building a segment beginning at index 0.
Continue extending the current segment character by character until the current segment has not been seen before.
Once the segment is unique, add it to your list of segments, mark it as seen, and begin a new segment from the next index.
Repeat until you reach the end of s.
Return an array of strings segments, where segments[i] is the ith segment created.

Example 1:

Input: s = "abbccccd"

Output: ["a","b","bc","c","cc","d"]



Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
'''

s = "abbccccd"

def PartitionString(s):
    seen_segments = set()
    segments = []
    start = 0
    end = 0

    while end < len(s):
        segment = s[start:end+1]

        if segment in seen_segments:
            end += 1

        else:
            segments.append(segment)
            seen_segments.add(segment)
            start = end + 1
            end = start
    
    return segments
print(PartitionString(s))

