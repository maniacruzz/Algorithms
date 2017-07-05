
def partition(arr,start,end):
    pivot=arr[start]
    left=start+1
    right=end

    done=False

    while not done:
        while left<=right and arr[left]<=pivot:
            left+=1
        while right>=left and arr[right]>=pivot:
            right-=1
        if right<left:
            done=True
        else:
            arr[left],arr[right]=arr[right],arr[left]
    arr[right],arr[start]=arr[start],arr[right]
    return right

def quickSortHelper(arr,start,end):
    if start<end:
        split=partition(arr,start,end)
        quickSortHelper(arr,start,split-1)
        quickSortHelper(arr,split+1,end)

def quickSort(arr):
    return quickSortHelper(arr,0,len(arr)-1)

def main():
    arr=[2,5,3,56,53,23,12,76,53,24,43,99,1]
    quickSort(arr)
    print(arr)
if __name__=="__main__":
    main()