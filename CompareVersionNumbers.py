class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        l1 = len(v1)
        l2 = len(v2)
        p = 0
        while l1 >= 0 and int(v1[l1-1]) == 0:
            l1 -= 1
        while l2 >= 0 and int(v2[l2-1]) == 0:
            l2 -= 1
        if l1==l2 and l1 == -1:
            return 0
        if l1 == -1:
            return -1
        if l2 == -1:
            return 1
        while p < l1 and p < l2:
            if int(v1[p]) > int(v2[p]):
                return 1
            if int(v1[p]) < int(v2[p]):
                return -1
            p += 1
        if p == l1 and p == l2:
            return 0
        if p < l1:
            return 1
        else:
            return -1
