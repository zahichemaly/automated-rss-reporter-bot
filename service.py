import json
import requests

BOT_TOKEN = ''
CHANNEL_ID = ''
FEED_URLS = []

def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
        global BOT_TOKEN
        global CHANNEL_ID
        global FEED_URLS
        BOT_TOKEN = config['bot_token']
        CHANNEL_ID = config['channel_id']
        FEED_URLS = config['feed_urls']

def get_message(entry, date):
    message = f"• {entry}"
    return message

def send_message(message):
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&text={message}&parse_mode=html")

def send_message_test(entry, source):
    message = get_message(entry, source)
    print(message)
