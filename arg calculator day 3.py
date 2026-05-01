def multiply_calc (first_numb, *others):
    total = first_numb
    
    for numb in others:
        total *= numb
    
    return total
    
print(multiply_calc(5,999))
