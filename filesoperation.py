import os

class filesOP():

	def __init__(self, episodefile, downloadedfile, savedir):
		self.episodefile = episodefile
		self.downloadedfile = downloadedfile
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

		if not os.path.isfile(self.downloadedfile): # check if downloaded file not exist
			print "Downloaded list file not available, creating one now.\n"
			self.writeToFile(self.downloadedfile, '')

	# open write data to file function
	def writeToFile(self, filepath, data):
		with open(filepath, 'w') as file:
			file.write(data)

