import sys

try:
    maxint = sys.maxint
except AttributeError:
    maxint = sys.maxsize

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        sort first, merge sort, O(m+n)
        """
        sorted = []
        iX, iY = 0, 0
        lengthX, lengthY = len(nums1), len(nums2)
        while iX < lengthX or iY < lengthY:
            if iX == lengthX:
                sorted.extend(nums2[iY:])
                break
            elif iY == lengthY:
                sorted.extend(nums1[iX:])
                break
            elif nums1[iX] <= nums2[iY]:
                sorted.append(nums1[iX])
                iX += 1
            else:
                sorted.append(nums2[iY])
                iY += 1
        if (lengthX + lengthY) %2 == 0:
            return (sorted[(lengthX + lengthY) / 2] + sorted[(lengthX + lengthY) / 2 - 1]) / 2.0
        return sorted[(lengthX + lengthY) / 2]

    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        log(min(m,n))
        1. find two partions, partionX and partionY
        2. make sure partitionX left <= partitionY right
        3. make sure partitionY left <= partitionX right
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        low, high = 0, len(nums1)
        maxLeftX, minRightX = 0, 0
        maxLeftY, minRightY = 0, 0
        lengthX, lengthY = len(nums1), len(nums2)
        while low <= high:
            partionX = (low + high) / 2
            partionY = (lengthX + lengthY + 1) / 2 - partionX
            maxLeftX = -maxint if partionX == 0 else nums1[partionX - 1]
            minRightX = maxint if partionX == lengthX else nums1[partionX]

            maxLeftY = -maxint if partionY == 0 else nums2[partionY - 1]
            minRightY = maxint if partionY == lengthY else nums2[partionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (lengthX + lengthY) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partionX - 1
            else:
                low = partionX + 1


if __name__ == "__main__":
    solution = Solution()
    print solution.findMedianSortedArrays1([1, 2, 4], [12, 34, 56])
    print solution.findMedianSortedArrays([1, 2, 4], [12, 34, 56])
    print solution.findMedianSortedArrays1([1, 2, 4], [12, 34, 56, 59])
    print solution.findMedianSortedArrays([1, 2, 4], [12, 34, 56, 59])
    print solution.findMedianSortedArrays1([], [12, 34, 56])
    print solution.findMedianSortedArrays1([12, 34, 56],[])
    print solution.findMedianSortedArrays([], [12, 34, 56])