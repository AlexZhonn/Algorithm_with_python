def countdown(i):  
    print(i)  
    if i <= 1: # base case  
        return   
    else:          
        countdown(i-1)  #recursive case
