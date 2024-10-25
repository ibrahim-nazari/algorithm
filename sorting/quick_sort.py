
def quick_sort(nums):
    if len(nums) <=1:
        return nums
    else:
        pivot=nums[len(nums)//2]
        left=[x for x in nums if x < pivot]
        right=[x for x in nums if x > pivot]
        return quick_sort(left) +[pivot] + quick_sort(right)




def main():
    nums=list(map(int,input().split(",")))
    result=quick_sort(nums)
    print(result)


if __name__ =="__main__":
    main()