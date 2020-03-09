#'w'=write mode, 'r'=read mode, 'a'=append mode, 'r+'=read and write
#if you omit the mode argument, default is read-only

#Reading an entire file:
with open ('textfile.txt') as file_object:
	contents = file_object.read()
print(contents)

#File Paths
with open('textfiles/filename.txt') as file_object:

#Absolute file paths:
file_path = '/home/ehmatthes/other_files/textfiles/filename.txt'
with open(file_path) as file_object:

#***Windows uses (\)backslash instead of (/)forward slash when displaying file paths

#Reading Line by Line
with open(filename) as file_object:
	for line in file_object:
	print(line)

#Making a list of lines from a file
#readlines() method takes each line and stores it in a list, which can be worked with
#after the with block ends

with open(filename) as file_object:
	lines = file_object.readlines() 

for line in lines:
	print(line.rstrip())


#Writing to a file
#Empty file:
with open(filename, 'w') as file_object: 
	file_object.write("I love programming.")
#**Can only write strings to a text file. For numerical data in a text file - need to convert to string using str()


#Writing multiple lines
#writes doesn't add new lines unless you tell it to
with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n") 
	file_object.write("I love creating new games.\n")


#Appending to a file
#when opened in append mode, content doesn't get erased. Lines will be added at the end
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	


