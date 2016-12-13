from HTMLParser import HTMLParser

class GetLinks(HTMLParser):

	def __init__(self,directoryurl):
		HTMLParser.__init__(self)  
		self.directoryurl = directoryurl
		self.links = [] # store the links in a list

	# this will handle what to do when it find the html opening tag <a>, to get links
	def handle_starttag(self,tag,attrs):
		if tag == "a": # if found <a> continue
			for (attribute, value) in  attrs:
				if attribute == "href": # get href value only
					fullurl =  self.directoryurl + value # append directory url to the value, to make complete url
					self.links.append(fullurl) # insert the url into list

	def getDownLinks(self):
		return self.links