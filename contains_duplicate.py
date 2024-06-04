class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False
        
"""
    
nums = [1, 2, 3, 3]

class Solution(object):
    def containsDuplicate(self, nums):
    
        # :type nums: List[int]
        # :rtype: bool
        
        hashset = set()

        for x in nums:  # loop iterates over each element, nums = [1, 2, 3, 3]
            if x in hashset:  # does this element exist in the hashset
                return True
            # print(x) #prints nums each elements
            hashset.add(x)  # adding each elements to set(set doesn't allows duplicates)
        return False

# Create an instance of the Solution class
solution = Solution()
# Call the containsDuplicate method and print the result
result = solution.containsDuplicate(nums)
print(result)  # This should print True because there is a duplicate (3) in the list


def dupli(nums):
    
    hashset = set()
    for x in nums:
        if x in hashset:
            return True
        hashset.add(x)
    return False

result = dupli([1, 2, 3, 3])

print(result)

"""


    


