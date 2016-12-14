# TV Series Downloader
- Python script to automate my daily tv series downloading. 
<br>Just a personal project as a medium to learn Python OOP
- Developed in Python 2.7

# Purpose
- Automate your daily routines of downloading new show episodes.
- Just run the script, it will check if there are new episodes or not.
- If it found new episodes, it will automatically download it for you.

# Requirement
- Python 2.7

# Installation
Download this project by clicking on ```Download ZIP``` under the ```Clone or download``` dropdown
<br> Or clone this project: ```https://github.com/afzafri/Python-TV-Series-Downloader.git```

# Usage
- Open the file ```main.py```
- Edit the required input:
  - ```URL``` : Website URL. This script only support website with "index of /" directory.
  - ```SERIES``` : Your tv show title. Must be same as the directory in the website
  - ```SEASON``` : Your tv show season. ex: S01. Also must be same as the directory in the website
  - ```QUALITY``` : Set your prefered video quality, 720p, 1080p, 480p. Also must refer to the files name in the website directory. Usually the file name will included with the quality type.
  - ```X265ENCODER``` : Set True you want video encoded with x265. This also must refer to the files name in the website directory.
- Open Terminal or Command Prompt in this project directory and run:
  - ```python main.py```
- Sit back, and let the script do the job for you

# License
This library is under MIT license, please look at the `LICENSE` file
