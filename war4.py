def sort_array(source_array):
    
    odd_n = sorted([num for num in source_array if num % 2 != 0])
    
    odd_i = 0
    
    result_arr = []
    
    for num in source_array:
        
        if num  % 2 != 0:
            
            result_arr.append(odd_n[odd_i])
            
            odd_i += 1
            
        else:
            
            result_arr.append(num)
            
    return result_arr
