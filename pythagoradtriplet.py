
def pythagoreantriplet(array):
    squarelist=dict()
    squarerootlist=dict()
    size=len(array)
    for a in array:
        sq=a*a
        squarelist[a]=sq
        squarerootlist[sq]=a

    for i in range(size):
        for j in range(i,size):
            sum=squarelist[array[i]]+squarelist[array[j]]
            if sum in squarerootlist:
                return (array[i],array[j],squarerootlist[sum])
    return None

def main():
    array=[1,2,3,4,5,6,7]

    result=pythagoreantriplet(array)
    print(result)

if __name__=="__main__":
    main()