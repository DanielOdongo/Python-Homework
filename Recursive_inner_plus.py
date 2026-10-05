def recursive_inner_plus(input_list):
    for item in input_list:
        if isinstance(item, list):
            return recursive_inner_plus(item)
            
            result = []
           
            for number in input_list:
                result.append(number + 1)
                
                return result
