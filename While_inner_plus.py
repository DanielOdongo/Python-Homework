def while_inner_plus(input_list):
    current_list = input_list
    while any(isinstance(item, list) for item in current_list):
        for item in current_list:
            if isinstance(item, list):
                current_list = item
                break 
               
                result = []
                
                for number in current_list:
                    result.append(number + 1)
                    
                    return result
                    
                    input_list = [1,2,3,4, [5,6,7,[8,9]]]
                    print(while_inner_plus(input_list))
