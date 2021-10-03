# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Brute force approach is looping thru the version and returning the first version of bad version: this will be O(n): since we should minize te number of calls of the API i do not think this approach is best.
        #Optimize Approach:
        # use binary search to find the bad version.We start with te middle if it is a bad version we update the last pointer to the middle> Return Start
        end = n
        start = 0
        while start < end:
            mid = (start + end)//2
            if (isBadVersion(mid)):
                end = mid
            else:
                start = mid+1
        return start