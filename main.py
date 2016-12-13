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

		for i in range(len(linksList)):
			print linksList[i] + "\n"

if __name__ == '__main__':
	SeriesDownloader().run()