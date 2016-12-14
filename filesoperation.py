import os

class filesOP():

	def __init__(self, episodefile, savedir):
		self.episodefile = episodefile
		self.savedir = savedir

	# check and create directory function
	def createDirectory(self):
		if not os.path.exists(self.savedir): # check if directory not exists
			print "\n-------------------------------------------------"
			print "\nSave directory not available, creating one now.\n"

			os.mkdir(self.savedir) # create new directory
			self.createListFile() # call function

			print "-------------------------------------------------\n"

	# check and create file function
	def createListFile(self):
		if not os.path.isfile(self.episodefile): # check if episode file not exist
			print "Episode list file not available, creating one now.\n"
			self.writeToFile(self.episodefile, '')

	# open write data to file function, use for creating new file
	def writeToFile(self, filepath, data):
		# open file. 'w' is open for writing
		with open(filepath, 'w') as file:
			file.write(data)

	# write content from list to file
	def writeListToFile(self, filepath, datalist):
		# open file, 'w' for writing
		with open(filepath, 'w') as file:
			for link in datalist:
				file.write(link + '\n') # write to file, append \n to end of line, for new line

	# read content from file into list
	def readListFromFile(self, filepath):
		output = [] # create new list

		# open file. 'r' is for reading. 't' refers to text mode
		with open(filepath, 'rt') as file:
			for line in file:
				output.append(line.replace('\n','')) # replace \n in the text file with nothing. We only want the link in the list
		# return the list
		return output



