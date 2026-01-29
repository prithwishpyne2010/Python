nums=[1,3,2,15,6,3,4,5]
largest=nums[0]
for i in nums:
    if largest<i:
        largest=i
print(largest)