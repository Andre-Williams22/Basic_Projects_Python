
def simple(num1, num2):
	# This gives the function something to do
	pass
	# num2 = 5 is a default parameter, which by default gives num2 the value of 5
def simple(num1, num2=5):
	print(num1, num2)

simple(2)
# A program that creates windows bcg = background color, w = white
def basic_window(width, height, font='TNR',
				bgc='w', scrollbar=True):
			print(width,height,font,bgc)



# the only thing you have to specify is width and height
# In order to modify you can just type in 'a'. Everything down here corresponds with the function above
basic_window(500,300, 'a')