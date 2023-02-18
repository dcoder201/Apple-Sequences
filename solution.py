#User function Template for python3

class Solution:
    def appleSequences(self, n, m, arr):
        # code here
        left = 0
        right = 0
        oranges = 0
        max_apples = 0
        while right < n:
            if arr[right] == 'O':
                oranges += 1
            while oranges > m:
                if arr[left] == 'O':
                    oranges -= 1
                left += 1
            if right - left + 1 > max_apples:
                max_apples = right - left + 1
            right += 1
        return max_apples    
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        temp = input().split()
        N = int(temp[0])
        M = int(temp[1])
        arr = input()

        ob = Solution()
        print(ob.appleSequences(N, M, arr))
