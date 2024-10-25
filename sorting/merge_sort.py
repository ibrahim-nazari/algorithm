


def merge_and_sort(left,right):
    l,r=0,0
    result=[]
    while l< len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l +=1
        else:
            result.append(right[r])
            r +=1
    result=result + left[l:]
    result=result + right[r:]
    return result

def merge_sort(nums):

    if len(nums) <2:
        return nums
    mid=len(nums)//2
    left=merge_sort(nums[:mid])
    right=merge_sort(nums[mid:])
    sorted_result=merge_and_sort(left,right)
    return sorted_result


def main():
    nums=list(map(int,input("Enter comma seperated number to sort: ").split(",")))
    result=merge_sort(nums)
    print(result)


if __name__ =="__main__":
    main()