import sys
import os
import subprocess
import sqlite3


import sys

try:
	conn = sqlite3.connect('ratings.db')
	c = conn.cursor()

	c.execute('''CREATE TABLE ratings
	             (URL text, read int, interesting int, local_text_path text, local_metadata_path text)''')

	conn.close()

# REALLY HACKY
except:
	pass

# Check that the requirements for running are present
# 	Spark NLP
#	Newspaper

# Look for local directories, make if needed.
try:
	os.mkdir("article storage")
	os.mkdir("metadata_storage")
except:
	pass
# Find out which sources are wanted. Serve up articles to confirm that it's the intended source
# Write sources to text file

with open('sources.txt', 'w') as sources_file:
	source_input = ""
	while source_input not in ["q", 'Q', 'QUIT', 'quit']:

		source_input = input("Add a source, or type Q to quit.\n")
		if source_input not in ["q", 'Q', 'QUIT', 'quit']:
			sources_file.write(source_input)
			print(source_input)
			print('wrote a source!')