def merge_sort(list):
    """ Takes overall O(n log n)"""    
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(list):
    """Takes overall O(log n)"""
    middle = len(list)//2
    
    left_half = list[:middle]
    right_half = list[middle:]
    
    return left_half, right_half     

def merge(left, right):
    """Runs in overall O(n) time"""
    l = []
    i=0
    j=0
        
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else: 
            l.append(right[j])
            j+= 1
   
    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l   

def verify_sorted(list):
    n = len(list)
    
    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])


alist = [62, 54]

l = verify_sorted(alist)
nlist = merge_sort(alist)
test = verify_sorted(nlist)

print(nlist)