#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#Given a string s, return true if it is a palindrome, or false otherwise.

#solution1: cheating solution using in-built libraries and use extra memory, abit faster than sol2, T.C:O(n), S.C:O(n)
def isPalindrome(s):
    newStr=""
    for character in s:
        if character.isalnum():
            newStr+=character.lower()
    return newStr == newStr[::-1]
#solution2: still uses extra memory when we create a new string and then reverse it to create a new one, T.C:O(n), S.C:O(n)
def isPalindrome2(s):
        newS=re.sub(r'[\W_]+|[\s]+', '', s)
        return newS.replace(" ","").lower() == newS[::-1].replace(" ","").lower()
#solution3: 2 pointer solution, T.C:O(n*2), S.C:O(1)

def isPalindrome3(s):
    l,r=0,len(s)-1
    while(l<r):
        #check if the char is alphaneumeric, if not shift indices
        if l<r and not isAlphnum(s[l]):
            l+=1
            continue
        if l<r and not isAlphnum(s[r]):
            r-=1 
            continue   
        if s[l].lower() != s[r].lower():
            return False
        l+=1
        r-=1
    return True
#you can also get rid of ord lib and it still works
def isAlphnum(c):
    return (ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z') 
            or ord('0')<=ord(c)<=ord('9'))

