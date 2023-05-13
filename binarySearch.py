# Question1: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
def search(nums, target):
        l,r=0,len(nums)-1
        while l<=r:
            #mid = (l+r) // 2
            #not a problem with python about overflow as in python int are unbounded and they can be infinitely large
            #but can occur in java and C++ so instead of finding mid like above we could do something like
            #take the distance between them and divide by 2 give us half of the distance and we can add left pointer
            mid = l + (r-l) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
            