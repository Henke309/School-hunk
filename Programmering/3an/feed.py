import feedparser
import webbrowser

feed = feedparser.parse("http://www.reddit.com/r/karlskoga/.rss")

for f in feed.entries:
    print(index, f.title, f.link)

inp 0 int(input("Skriv in vilken nyhet du vill läsa!"))
webbrowser.open(feed.entries[inp].link)