#speed searching
import random
import time
def naive_search(l,target):
    for i in range(len(l)):
        if l[i]==target:
            return i
    
    return -1

def binary_search(list,target,low=None,High=None):
    if low is None:
        low=0
    if High is None:
        High=len(list)-1

    if High<low:
        return -1
    
    midpoint=(low+High)//2 #rounds automatically

    if list[midpoint]==target:
        return midpoint
    elif target<list[midpoint]:
        return binary_search(list,target,low,midpoint-1)
    else:
        #target> midpoint
        return binary_search(list,target,midpoint+1,High)
    
if __name__=="__main__":
    """
    l=[1,3,5,10,7,12]
    target=7
    print(naive_search(l,target))
    print(binary_search(l,target))

    """
    length=10000
    sorted_list=set()
    while len(sorted_list)<length:
        sorted_list.add(random.randint(-3*length,3*length))
    sorted_list=sorted(list(sorted_list))

    start=time.time()
    for target in sorted_list:
        naive_search(sorted_list,target)
    end=time.time()
    print("Naive search time: ",(end-start)/length,"seconds")

    start=time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end=time.time()
    print("binary search time: ",(end-start)/length,"seconds")
