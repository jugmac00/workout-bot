import os
from pathlib import Path
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
    wod_div = parser.find("div", attrs={"class": "custom darewod"})
    wod_img = Path(wod_div.a["href"]).relative_to("/").with_suffix(".jpg")
    img_path = Path("/images")
    return urljoin(DAREBEE_URL, str(img_path / wod_img))


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
