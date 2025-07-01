# https://leetcode.com/problems/first-bad-version/description/

# 278. First Bad Version

def git_bisect(branch):
    '''
    Show the starting index where an error may occur in a history of commits.
    1 = Working commit
    0 = Error commit

    Constraints:
    "Working commits" will always be on the "left" of the branch.
    "Error commits" will always be on the "right" of the branch.
    It is possible to have "all working" or "all error" commits in a branch.

    Return Values:
    -1 = No error commit exists in this branch
    Any other integer is the index where the first error commit occurs.
    '''
    if branch[-1] == 1: return -1
    if branch[0] == 0: return 0
    
    # Perform binary search - Time: O(logn)  Space: O(1)
    low = 0
    high = len(branch) - 1

    while low < high - 1:
        mid = (high + low) // 2
        if branch[mid] == 1:
            low = mid
        else:
            high = mid
    return high
    

if __name__=="__main__":
    print("Index:", git_bisect([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]))