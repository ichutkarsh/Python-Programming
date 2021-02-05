#To find duplicate values in an array

# in O(N) Running time complexity
# values in an array not mare than its length

def is_duplicate(nums):
     for num in nums:
         if nums[abs(num)] >= 0:
             nums[abs(num)] = -nums[abs(num)]

         else:
             print(f"the duplicate number is {abs(num)}")

if __name__ == '__main__':

    lst = [2,5,1,2,3,1,4,3]
    print(is_duplicate(lst))
