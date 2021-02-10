from workout_bot.main import extract_dailydare_url
from workout_bot.main import extract_wod_url

# Please note, that the following tests are just smoke tests in order
# to start testing.
# Yes, they rely on a website which is not under my control.
# Yes, I know, this is not good.
# This won't be permanent.


def test_extract_dailydare_url():
    URL = extract_dailydare_url()
    assert URL.startswith("https://www.darebee.com/images/promo/dares/")


def test_extract_wod_url():
    URL = extract_wod_url()
    assert URL.startswith("https://www.darebee.com/images/workouts/")
