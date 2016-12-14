import fetchwebpage
import getlinks
import filesoperation
import os

class SeriesDownloader():

	# the show details, class var
	URL = "" # website url, only index directory (no webpage) supported
	SERIES = "The Flash" # show name, must be same as the show directory name
	SEASON = "S03" # show season, also must be same as the directory name
	QUALITY = "720p" # video quality, 1080p, 720p, 480p (refer to the file name)
	X265ENCODER = True # True if want to download the x265 encoded video. note: also refer to the file name if available or not
	DIRECTORYURL = URL + SERIES + "/" + SEASON + "/" # complete download directory url 
	SAVEDIRECTORY = "./" + SERIES.replace(' ','_') + "_" + SEASON + "/" # save directory
	EPISODES_LIST = SAVEDIRECTORY + SERIES.replace(' ','_') + '_' + SEASON + '_Episodes.txt' # text file for saving the episodes list
	DOWNLOADED_LIST = SAVEDIRECTORY + SERIES.replace(' ','_') + '_' + SEASON + '_Downloaded.txt' # text file for saving the downloaded episodes
	
	def run(self):
		
		# for checking if save directory and files available, if not, create new one
		checkDirFile = filesoperation.filesOP(self.EPISODES_LIST, self.DOWNLOADED_LIST, self.SAVEDIRECTORY)
		checkDirFile.createDirectory()

		# for fetching the webpage HTML
		print "\n---------------------------------------"
		print "\nFetching download links...please wait\n"
		print "---------------------------------------\n"
		getHTML = fetchwebpage.FetchWeb(self.DIRECTORYURL) # create object
		pageHTML = getHTML.run()

		# for extracting (parse) the DOWNLOAD LINKS from the webpage HTML
		getLinks = getlinks.GetLinks(self.DIRECTORYURL, self.QUALITY, self.X265ENCODER) # create object
		getLinks.feed(pageHTML)
		linksList = getLinks.getFilteredDownLinks()

		for i in range(len(linksList)):
			print linksList[i] + "\n"

		print "\n---------------------------------------"
		print "\n" + str(len(linksList)) + " episodes available for " + self.SERIES + " " + self.SEASON
		print "\n---------------------------------------\n"
		
if __name__ == '__main__':
	SeriesDownloader().run()