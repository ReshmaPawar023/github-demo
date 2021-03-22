#add 
def add(x,y):
    return x+y
	
	
#subtract
def subtract(x,y):
    if y>x:
		return NEGATIVE_VALUE_ERROR
	else:
		return x-y
		

#multiply
def multiply(x,y):
    pass
	
	
#divide
def divide(x,y):
	if y==0:
		return DIVIDE_BY_0_ERROR
		
	else:
		return  x/y
