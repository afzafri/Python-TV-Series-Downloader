import urllib2

class FetchWeb():

	def __init__(self,directoryurl):
		self.directoryurl = directoryurl

	def run(self):
		openUrl = urllib2.urlopen(self.directoryurl) # open the url
		getUrl = openUrl.read() # read/get the html
		return getUrl