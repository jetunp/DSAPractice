#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
import collections
#solution1: using hashmap to keep the count of letters in each string T.C:O(s+t), S.C:O(s+t)
def isAnagram( s: str, t: str) -> bool:
    
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


