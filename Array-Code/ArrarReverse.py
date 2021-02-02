# Reverse of an array in-place

def reverseArray(nums):

    #start inddex
    startindex = 0
    #end index
    endindex = len(nums) - 1

    #iterating through the array
    while startindex<endindex :
        nums[startindex],nums[endindex] = nums[endindex],nums[startindex]
        startindex += 1
        endindex -= 1

if __name__ == '__main__':
    
    n = [1,2,3,4]
    reverseArray(n) 
    print(n)