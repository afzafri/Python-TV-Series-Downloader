from HTMLParser import HTMLParser # for parse HTML 

# create new subclass of HTMLParser
class GetLinks(HTMLParser):

	def __init__(self, directoryurl, quality, encoder):
		HTMLParser.__init__(self)  # inherit HTMLParser class
		# store the received parameters into variable
		self.directoryurl = directoryurl 
		self.quality = quality
		self.encoder = encoder
		self.links = [] # store the links in a list

	# this will handle what to do when it find the html opening tag <a>, to get links
	def handle_starttag(self, tag, attrs):
		if tag == "a": # if found <a> continue
			for (attribute, value) in  attrs: # loop through the tag
				if attribute == "href": # get href value only
					fullurl =  self.directoryurl + value # append directory url to the value, to make complete url
					self.links.append(fullurl) # insert the url into list

	# filter list, we only want to get episode that match our Quality and encoder
	# then return the list
	def getFilteredDownLinks(self):
		# create list
		self.filteredList = []
		# iterate through the list
		for i in range(len(self.links)):
			links = self.links[i]

			# check if filter x265 encoder is set to True
			if self.encoder == True:
				# check if quality and encoder is in the links, add to the list
				if self.quality in links and "x265" in links:
					self.filteredList.append(links)
			else: 
				# if encoder False, only check quality
				if self.quality in links:
					self.filteredList.append(links)

		return self.filteredList # return the list

		