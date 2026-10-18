#class Solution:
def removeElement(nums: list[int], val: int) -> int:
    k = 0
    for reader in range(len(nums)):
        if nums[reader] != val:
            nums[k] = nums[reader]
            k += 1
    return k


nums = [3,2,2,3]
val = 3
k = removeElement(nums, val)
print(f"k = {k}, modfified nums = {nums[:k]}")
#print(val)
#print(f"k = {k}, modified nums = {nums[:k]}")


#print(Input)