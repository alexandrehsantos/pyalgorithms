def find_minimal_value(list):
    minimal_index = 0
    for index in range(len(list)):
        if list[index] <list[minimal_index]:
            minimal_index = index
    return minimal_index;

def selection_sort(list):
    sorted_list = []
    print("%-25s %-25s" % (list, sorted_list))
    for i in range(len(list)):
        minimal_index = find_minimal_value(list)
        sorted_list.append(list.pop(minimal_index))
        print("%-25s %-25s" % (list, sorted_list  ))
    return sorted_list    

    
list = [234,34,46545,67657,222,3,23,4,5,6]  
value = selection_sort(list)       
print(value)    
            
            
            