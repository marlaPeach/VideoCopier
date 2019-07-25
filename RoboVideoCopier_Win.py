#!/usr/bin/env python3
import shutil
import os
import datetime
from send2trash import send2trash

def main():
	directory= os.fsencode('C:\\Users\\schmidttl\\Documents\\TestFolder')
	dst= 'C:\\Users\\schmidttl\\Documents\\DestinationFolder'
	logname='C:\\Users\\schmidttl\\Documents\\Copier_Log'
	date = datetime.date(2019, 7, 22)
	if(len(os.listdir(directory))==0):
		with open(logname, 'a') as log:
			log.write('\n')
			log.write(str(date))
			log.write(' No files in video directory.')
	else:
		for file in os.listdir(directory):
			filename=os.fsdecode(file)
			inpath= os.fsdecode(directory)
			src = inpath + "\\" + filename
			if(filename.endswith('.mp4')):
				shutil.copy2(src, dst)
				with open(logname, 'a') as log:
					log.write('\n')
					log.write(str(date))
					log.write(' ' + filename + ': Video copied successfully. Moving old item to trash.')
				send2trash(src)
			else:
				with open(logname, 'a') as log:
					log.write('\n')
					log.write(str(date))
					log.write(' ' + filename + ': Non video file moved to trash.')
				send2trash(src)
		with open(logname, 'a') as log:
			log.write('\n')
			log.write('Video Directory is fully copied to Transcoder and newly empty.')

if __name__ == '__main__':
    main()