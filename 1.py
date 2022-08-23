# class abc():
#     a=1
#     b=2
#     @classmethod
#     c=4
#
# abc=abc()
# print(abc.a)


nums=[1,2,3,4,5,6,7]
k=3
k=k%len(nums)
print(nums[-k:],nums[:-k])
nums=nums[-k:]+nums[:-k]
print(nums)
print(nums==nums[:])

# nums=[1,2,3,4,5,6,7]
# res=[]
# res.append(nums[:])
# nums[0],nums[6]=nums[6],nums[0]
# res.append(nums[:])
# print(res)
