import fetchwebpage
import getlinks
import filesoperation
import download

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
	
	def run(self):

		# intro
		print "\n---------------------------------------"
		print "\nTV Series Downloader - Automate your download"
		print "\nPython Script - Afif Zafri 2016"
		print "\n---------------------------------------\n"
		
		# for checking if save directory and files available, if not, create new one
		fileOPobj = filesoperation.filesOP(self.EPISODES_LIST, self.SAVEDIRECTORY) # create new object
		fileOPobj.createDirectory() # call method

		# create new list
		episodesList = [] 	
		# read file, store into list
		episodesList = fileOPobj.readListFromFile(self.EPISODES_LIST)

		# for fetching the webpage HTML
		print "\n---------------------------------------"
		print "\nFetching episodes...please wait\n"
		print "---------------------------------------\n"
		getHTML = fetchwebpage.FetchWeb(self.DIRECTORYURL) # create object
		pageHTML = getHTML.run()

		# for extracting (parse) the DOWNLOAD LINKS from the webpage HTML
		getLinks = getlinks.GetLinks(self.DIRECTORYURL, self.QUALITY, self.X265ENCODER) # create object
		getLinks.feed(pageHTML)
		linksList = getLinks.getFilteredDownLinks() # receive episode links, store into a list

		newEpisodeList = [] # new list for adding new episode that not available in episodes file
		newEp = 0 # var to store number of new episode

		# to get number of new episode
		# if there is new episode, store into new episode list
		if len(linksList) >= len(episodesList):
			newEp = len(linksList) - len(episodesList)

			for i in range(len(linksList)):
				if linksList[i] not in episodesList:
					newEpisodeList.append(linksList[i])

		print "\n---------------------------------------"
		print "\n" + str(len(linksList)) + " episodes available for " + self.SERIES + " " + self.SEASON
		print "\n" + str(newEp) + " new episodes."
		print "\n---------------------------------------\n"

		# check if no new episode, display message
		# if new episode available, download it
		if not newEpisodeList:
			print "\nNo new episode available to be downloaded. Please run this program again later.\n"
		else:
			downobj = download.downloadFile(self.SAVEDIRECTORY) # initialize object, pass in the save directory
			for x in range(len(newEpisodeList)):
				downobj.startDownload(newEpisodeList[x]) # call class method, pass in the download url

			# when finished, write the new list of episode (old ep + new ep) into the episode file
			fileOPobj.writeListToFile(self.EPISODES_LIST,(episodesList + newEpisodeList))
			print "\nAll new episodes have been downloaded. Enjoy \n"

if __name__ == '__main__':
	SeriesDownloader().run()