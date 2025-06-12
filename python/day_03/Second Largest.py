arr = [12, 35, 1, 10, 34, 1]
def getSecondLargest(arr):
        # Code Here
        if len(arr) < 2:
            return -1
        
        uniwue_arr = list(set(arr))
        if len(uniwue_arr) < 2:
            return -1
        
        uniwue_arr.sort()
        return uniwue_arr[-2]

print(getSecondLargest(arr))