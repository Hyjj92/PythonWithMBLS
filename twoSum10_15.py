def twoSum( nums, target) :
        for i in range( 0,len(nums)  ):
            for j in range ( i+1,len(nums)  ):
                if target == nums[i] + nums[j]:
                    print('[', i, ',' ,j , ']')
num = [2,7,11,15]
target = 9
twoSum(num,target)
print('over')