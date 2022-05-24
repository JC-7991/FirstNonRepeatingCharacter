def first_non_repeating_letter(string):
    
    lower = string.lower()     
    
    for i, x in enumerate(lower):         
        if lower.count(x) == 1:             
            return string[i]
        
    return ""