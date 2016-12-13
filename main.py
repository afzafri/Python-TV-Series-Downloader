import fetchwebpage
import getlinks

class SeriesDownloader():

	# the show details, class var
	URL = "" # website url, only index directory (no webpage) supported
	SERIES = "The Flash" # show name, must be same as the show directory name
	SEASON = "S03" # show season, also must be same as the directory name
	QUALITY = "720p" # video quality, 1080p, 720p, 480p (refer to the file name)
	X265ENCODER = True # True if want to download the x265 encoded video. note: also refer to the file name if available or not
	DIRECTORYURL = URL + SERIES + "/" + SEASON + "/" # complete url 
	EPISODES_LIST = SERIES.replace(' ','_') + '_' + SEASON + '_Episodes.txt' # text file for saving the episodes list
	DOWNLOADED_LIST = SERIES.replace(' ','_') + '_' + SEASON + '_Downloaded.txt' # text file for saving the downloaded episodes
	
	def run(self):
		# for fetching the webpage HTML
		print "\nGetting page...please wait"
		getHTML = fetchwebpage.FetchWeb(self.DIRECTORYURL) # create object
		pageHTML = getHTML.run()

		# for extracting (parse) the DOWNLOAD LINKS from the webpage HTML
		print "\nGetting download links...please wait"
		getLinks = getlinks.GetLinks(self.DIRECTORYURL) # create object
		getLinks.feed(pageHTML)
		linksList = getLinks.getDownLinks()
		filteredList = self.filterEp(linksList)

		for i in range(len(filteredList)):
			print filteredList[i] + "\n"

	# filter list, we only want to get episode that match our Quality and encoder
	def filterEp(self, linksList):
		# create list
		filteredList = []
		# iterate through the list
		for i in range(len(linksList)):
			links = linksList[i]

			# check if filter x265 encoder is set to True
			if self.X265ENCODER == True:
				# check if quality and encoder is in the links, add to the list
				if self.QUALITY in links and "x265" in links:
					filteredList.append(links)
			else: 
				# if encoder False, only check quality
				if self.QUALITY in links:
					filteredList.append(links)

		return filteredList # return the list






if __name__ == '__main__':
	SeriesDownloader().run()