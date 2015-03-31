# GroovebackupPlus
A helpful tool for restoring lost songs that get taken down from Grooveshark.

Note: this was built for personal use, so it only runs on Linux. Feel free to copy this code and port it for windows. Also, I have only tested it with Python 2.7.

### Step 1:
Go to http://www.groovebackup.com

### Step 2:
Export your collection

### Step 3:
Save the file in your backups folder in YYYY-MM-DD format, e.g. "2015-03-30". If you feel the need to make multiple backups in the same day, just append a "-1", "-2" etc.

### Step 4 (you need at least two backups for this two work):
Run groovebackup.py

### Step 5:
Open up the newly created file and see all the songs that have been removed or added since your last backup.

## Notable limitations
It is impossible to detect if you have added a song and it is removed before you can backup your collection :(

Also the current code will improperly display songs with commas in their name/artist/album.

If the output format is annoying for you, remember that you can press tab to autocomplete in terminal. If you don't know how to use terminal, just use a file browser program. What are you doing on github without knowing how to use terminal anyway?


