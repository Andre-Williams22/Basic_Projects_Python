# A global variable is a variable that can be accessed anywhere
# A local variable can only be accessed in its environment
# this variable has no parent function and has no global variable
x = 6 
# Here we're able to access x from this function, but x is not a global variable. It is a local variable
def example():
	
	print(x)
	print(x+5)

example()


# This is a global variable
w = 9

def life():
	global w 
	print(w)
	w+ = 8
	print(w)

life()

# Some teachers or companies don't like using global variables like the cto of a company or something.
#This is how you get around it !!!!
y = 7

def code():
	globy = y
	print(globy)
	globy+=4
	print(globy)
	# So we're not able to access globy outside this function, making it local
	# So if we have multiple functions and we want them to work together they can't because it's a local variable
	# The Solution is return 
	return globy

y = code()

print(y)
# This is how you modify this by not using a global variable and allowing different functions to work together