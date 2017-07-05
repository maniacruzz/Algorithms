def merge(a,b):
    res=[]
    while a and b:
        if a[0]<b[0]:
            res.append(a[0])
            a.pop(0)
        else:
            res.append(b[0])
            b.pop(0)
    if a:
        res+=a
    else:
        res+=b
    return res

def mergeSort(arr):
    if not arr or len(arr)==1:
        return arr
    middle=len(arr)//2
    left=mergeSort(arr[:middle])
    right=mergeSort(arr[middle:])
    arr=merge(left,right)
    return arr

def main():
    arr=[2,5,3,56,53,23,12,76,53,24,43,99,1]
    result=mergeSort(arr)
    print(result)
if __name__=="__main__":
    main()