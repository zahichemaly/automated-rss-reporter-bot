import feedparser
import json
import service as api
import util as util

def main():
    for feed_url in api.FEED_URLS:
        rss_feed = feedparser.parse(feed_url)
        source = rss_feed.feed.title
        today = util.get_date_today().date()
        message = ""
        for entry in rss_feed.entries:
            entry_name = entry.title
            entry_date = entry.published
            published_date = util.get_date(entry_date).date()
            if (published_date == today):
                message += api.get_message(entry_name, entry_date) + "\n\n"
        api.send_message(message)

if __name__ == "__main__":
    api.load_config()
    main()
