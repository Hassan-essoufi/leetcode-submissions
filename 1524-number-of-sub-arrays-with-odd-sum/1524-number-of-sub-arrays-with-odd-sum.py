class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        even_count = 1
        odd_count = 0
        prefix = 0
        answer = 0
 
        for num in arr:
            prefix += num

            if prefix % 2 == 1:
                answer += even_count
                odd_count += 1
            else:
                answer += odd_count
                even_count += 1
        return answer % (10**9 + 7)
                

            

        