class Solution:
    def isPalindrome(self, s: str) -> bool:
        coll = ""
        for i in s:
            if i.isalnum():
                coll += i.lower()
        i = 0
        j= len(coll)-1
        while i < j:
            if coll[i] != coll[j]:
                return False
            i+=1
            j-=1
        return True
