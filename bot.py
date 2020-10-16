import feedparser
import json
import service as api
from datetime import datetime as dt
from datetime import timezone

def main():
    for feed_url in api.FEED_URLS:
        rss_feed = feedparser.parse(feed_url)
        today = dt.now().date()
        for entry in rss_feed.entries:
            entry_name = entry.title
            entry_date = entry.published
            published_date = get_date(entry_date)
            if (published_date == today):
                api.send_message(entry_name, rss_feed.feed.title)

def get_date(dateString):
    #Date Format in feed
    #Fri, 10 Jul 2020 13:48:41 +0000
    trimmedDate = dateString[:-6]
    return dt.strptime(trimmedDate, "%a, %d %b %Y %H:%M:%S").date()

if __name__ == "__main__":
    api.load_config()
    main()
