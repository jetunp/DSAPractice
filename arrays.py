#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
import collections
#solution1: using hashmap to keep the count of letters in each string T.C:O(s+t), S.C:O(s+t)
def isAnagram( s, t):
    
    #if they are the same length they cannot be anagrams
    if len(s) != len(t): 
        return False
    #create 2 dictionaries, these keep the count of letters in each string like {'a':2}
    dictS,dictT={},{}
    for i in range(len(s)):
        print("in first for")
        #dict[key]=value
        #.get() method checks if key not exist, default is set to 0s
        dictS[s[i]] = 1 + dictS.get(s[i],0)
        dictT[t[i]] = 1 + dictT.get(t[i],0)
    for i in dictS:
        print("in second for")
        #check if the count of each letter in both strings same or not
        #if not then we return false rightaway
        if dictS[i] != dictT.get(i,0):
            print("in second if")
            return False
    return True
#solution2:use counter function T.C:O(s+t) S.C:O(s+t)
    #return collections.Counter(s) == collections.Counter(t)

#solution3: sort the strings and compare T.C:O(nlogn) S.C:O(1) mostly
    #return sorted(s) == sorted(t)


#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#solution1: T.C:O(n*2), S.C:O(1)
def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

#solution2: using a hashmap and target-nums check
def twoSum(nums, target):
        dict = {} #val:index
        #now we can add all the elements to the dict before traversing
        #through it and checking for target-number in the dict
        #but clever way: initially say our hashmap is empty and we check each element for
        #target-number and if it does not exist in hashmap we add {"val":index} in dict and 
        #move on untill we find the diff number we want
        # for i in range(len(nums)):
        #     if target-nums[i] in dict:
        #         return [dict[target-nums[i]],i]
        #     else:
        #         dict[nums[i]]=i
        #or using enumerate fn
        for i,n in enumerate(nums):
            if target-n in dict:
                return [dict[target-n],i]
            else:
                dict[n]=i


# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

#solution1: T.C:O(n) S.C:O(set1+set2)
def findDifference(nums1, nums2):
    answer1, answer2= set(),set()
    for i in range(len(nums1)):
        if nums1[i] not in nums2:
            answer1.add(nums1[i])
    for i in range(len(nums2)):
        if nums2[i] not in nums1:
            answer2.add(nums2[i])

    return [answer1,answer2]
#solution2: one liner 
    return [(set(nums1)-set(nums2)),(set(nums2)-set(nums1))]


#bubble sorting
def bubbleSort(arr):
    swapped=False
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                swapped = True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if not swapped:
            return 
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
 
print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")