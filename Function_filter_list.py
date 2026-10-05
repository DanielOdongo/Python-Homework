def filter_list(numbers, threshold):
    result = []
    
    for number in numbers:
        if number <= threshold:
            result.append(number)
           
            return result
