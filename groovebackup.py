from os import listdir
from os.path import isfile, join
from datetime import datetime

############################################
#			//TODO
# - Bugs
#   + Fix parsing on strings with extra
#		commas
#   + Sometimes songs end up in removed AND
#		in added... no idea why
#
# - Features (besides the ones that are bugs)
#	+ (ambitious) Input username and pw,
#		fetches data from groovebackup and
#		automatically runs
#	+ (ambitious) GUI?
#	+ Some sort of nicer output format
#	+ Strip the "" from words
#	+ Optimize?
#
# - Other
#	+ Contact grooveshark devs about this
#		proj, see if they want to help
#	+ Figure out how to use grooveshark API
#
#


#################################
# Class Song 
# Somewhat unnecessary but it helps with sorting/storing/printing

class Song(object):
	def __init__(self, SongName, ArtistName, AlbumName):
		self.SongName = SongName
		self.ArtistName = ArtistName
		self.AlbumName = AlbumName
	def __repr__(self):
		return '{}--{}--{}'.format(self.SongName,
                                  self.ArtistName,
                                  self.AlbumName)
	def getName(self):
		return self.SongName
	def getArtist(self):
		return self.ArtistName
	def getAlbum(self):
		return self.AlbumName

###############################
# 		 LOCATE FILES		  #
onlyfiles = [f for f in listdir("backups") if isfile(join("backups",f))]
onlyfiles.sort()
# get the most recent two
# store files as YYYY-MM-DD
recent2 = onlyfiles[len(onlyfiles)-2:]

songsA = [] # becomes "removed"
songsB = [] # becomes "added"

###############################
# 		   INPUT+PARSE		  #
f1 = open(join("backups",recent2[0]),'r')

for i,line in enumerate(f1):
	parsed = line.strip().split(',')
	songsA.append(Song(parsed[0],parsed[1], parsed[2]))

f1.close()

f2 = open(join("backups",recent2[1]),'r')

for i,line in enumerate(f2):
	parsed = line.strip().split(',')
	b = Song(parsed[0],parsed[1], parsed[2])
	flag = 0
	for j,a in enumerate(songsA):
		if str(a) == str(b):
			flag = 1
			songsA.remove(a)
			break
	if flag == 0:
		songsB.append(b)

f2.close()

###############################
# 			OUTPUT			  #

# if this output format annoys you, go ahead and change it
out = open(str(datetime.now()),'w')
out.write("Removed\n")

for i in sorted(sorted(songsA, key=Song.getAlbum), key=Song.getArtist):
	out.write(str(i) + '\n')

out.write("Added\n")

for i in sorted(sorted(songsB, key=Song.getAlbum), key=Song.getArtist):
	out.write(str(i) + '\n')

out.close()


