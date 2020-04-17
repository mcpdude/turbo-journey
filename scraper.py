import newspaper
import sqlite3
import sys

conn = sqlite3.connect('ratings.db')
c = conn.cursor()





# Read in sources in sources.txt

with open('sources.txt') as sources_file:
	sources = sources_file.read()
	source_list = []
	for line in sources.split('\n'):
		if len(line.strip()) != 0:
			print(line)
			source_list.append(line)

# Download articles from the sources

articles = {}
for source in source_list:
	articles[source] = newspaper.build(source, memoize_articles=False)
	print(articles[source].size())

for article_source in articles:
	

	for story in articles[article_source].articles:
		story.download()
		story.parse()
		# store a copy of the text locallly
		with open(story.title, 'w+') as local_copy:
			local_copy.write(story.text)

		# offer the story to the reader
		print(story.text)

		# Get their thoughts
		interesting = input("Did you find this article interesting? [Y/N]\n")
		if 'y' in interesting.lower():
			interesting = 1
		else:
			interesting = 0
		c.execute('''INSERT INTO ratings VALUES(?, 1, ?, ?, ?)''', [story.url, interesting, "article storage/" + story.title, "article metadata/"+ story.title])
		conn.commit()


# Store URLs in SQLite db

# Parse articles and determine how interesting they are by calling sparknlp on them

# Serve links to user, one at a time, and ask if they were interesting or not. 
