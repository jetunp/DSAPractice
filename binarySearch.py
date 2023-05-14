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

#question2: Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 #Solution1: brute force : T.C: O(mn) S.C: O(m+n)
# def countNegatives(grid):
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] < 0:
#                     count+=1

#         return count 


#solution2: two-pointer solution  
# Time: O(n + m) Space: O(1)
#this is based on number of rows and pointer to index of last row
        # row = len(grid)-1
        # #column
        # column = 0
        # # keeps count of the negative numbers 
        # count = 0
        # # i conditions makes loop through all rows of grid and j condition makes loop within each elem.
        # while row>=0 and column < len(grid[0]): #O(n)+O(m)
        #     if grid[row][column] < 0:
        #         count+=len(grid[0])-column
        #         row-=1
        #     else:
        #         column+=1
        # return count 

#soluion3: binary search T.C: O(mlogn)
def countNegatives(grid):
        count = 0 
        for row in grid:
            count += bin(row)
        return count
def bin(row):
        l=0
        h=len(row)-1
        while l<=h:
            mid = l+(h-l) // 2
            if row[mid] < 0:
                h = mid -1
            else:
                l = mid +1
        return len(row)-l
# grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# print(countNegatives(grid))

#Question3: Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
#In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.

#Solution1: BruteForce T.C: O(n) S.C:O(1)
def maximumCount(nums) :
        pos = 0
        neg = 0
        for num in nums:
            if num == 0:
                continue
            elif num > 0:
                pos += 1
            else:
                neg += 1
        return max(pos,neg)

#solution2: Binary search: O(logn)
def binarySearch(nums,target):
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
    def maximumCount(nums):
        return max(binarySearch(nums,0),len(nums)-binarySearch(nums,1))