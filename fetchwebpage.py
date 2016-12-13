import urllib2 # library to get content of webpage

class FetchWeb():

	def __init__(self,directoryurl):
		self.directoryurl = directoryurl # store receive url into variable

	def run(self):
		openUrl = urllib2.urlopen(self.directoryurl) # open the url
		getUrl = openUrl.read() # read/get the html
		return getUrl # return the html content