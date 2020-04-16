import newspaper
import sqlite3

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
	stories_count = articles[article_source].size()

	for i in range(stories_count):
		story = articles[article_source].articles[i]
		story.download()
		story.parse()
		print(story.text)

# Store URLs in SQLite db

# Parse articles and determine how interesting they are by calling sparknlp on them

# Serve links to user, one at a time, and ask if they were interesting or not. 
