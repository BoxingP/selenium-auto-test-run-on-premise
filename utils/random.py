import random
from time import sleep


def random_browser():
    browser_list = ['chrome', 'edge', 'firefox']
    selected_browser = random.choice(browser_list)
    print(f"Using {selected_browser} to do the test.")
    return selected_browser


def random_sleep():
    start = round(random.random(), 1) * 10
    stop = random.randint(60, 120)
    seconds = round(random.uniform(start, stop), 5)
    print(f"Random sleeping {seconds} seconds ...")
    sleep(seconds)
