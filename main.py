import os
from urllib.parse import urljoin

import httpx
import telegram
from bs4 import BeautifulSoup

DAREBEE_URL = "https://www.darebee.com/"
API_KEY = os.getenv("API_KEY")
TELEGRAM_ID = os.getenv("TELEGRAM_ID")


def get_source_code(url):
    r = httpx.get(url)
    return r.text


def get_parser(html):
    return BeautifulSoup(html, "html.parser")


def extract_dailydare_url():
    html = get_source_code(url=DAREBEE_URL)
    parser = get_parser(html)
    dailydare_div = parser.find('div', attrs={"class": "custom dailydare"})
    dailydare_img = dailydare_div.img['src']
    return urljoin(DAREBEE_URL, dailydare_img)


def extract_wod_url():
    html = get_source_code(url=DAREBEE_URL)
    parser = get_parser(html)
    wod_div = parser.find('div', attrs={"class": "custom darewod"})
    wod_name = wod_div.a['href'].split('/')[2].split('.')[0]
    img_path = '/images/workouts/'
    wod_img = wod_name + '.jpg'
    path = os.path.join(img_path, wod_img)
    return urljoin(DAREBEE_URL, path)


if __name__ == '__main__':
    if TELEGRAM_ID is not None and API_KEY is not None:
        bot = telegram.Bot(token=API_KEY)

        dailydare_url = extract_dailydare_url()
        bot.send_photo(chat_id=int(TELEGRAM_ID), photo=dailydare_url)

        wod_url = extract_wod_url()
        bot.send_photo(chat_id=int(TELEGRAM_ID), photo=wod_url)
    else:
        print("Missing API_KEY or TELEGRAM_ID.")
        print("Please make sure to load environment variables.")
