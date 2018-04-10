#!/usr/bin/python

# define a complex list and an empty temporary list 
source_list = [1, 2, 3, 4, [1, 2, 3, [4, 5, 6, ]]]
temp_list = []

# recursive subroutine to be called any time an array/list is found
def flatten(in_list):

	# iterate through the list, test if each element is a list
	for elem in in_list:

		# if the element is a list, call the 'flatten' sub
		if (isinstance (elem, list)):
			flatten(elem)

		# other wise, just append it to our temp list
		else:
			temp_list.append(elem)
		

print "Start"
print "source_list is " + str(source_list)

# call the 'flatten' sub for the original list
flatten(source_list)

# once we are done we move the temp list into the original list
source_list = temp_list

print "Now source_list is " + str(source_list)
print "OK"
