import requests
from bs4 import BeautifulSoup
import sys
import random

def get_user_agent():
    try:
        lines = [line.rstrip("\n") for line in open("useragent.txt")]
    except IOError as e:
        print("User Agent error: %s" % e.strerror)
        sys.exit(1)
    return lines


def dorkFind():
    try:
        usrr = get_user_agent()
        header = {"User-Agent": "{}".format(random.choice(usrr))}
        print("e.g---->inurl:\"search.php?q=\"")
        aranacak = input("Please enter your dork:")
        for x in range(0, 20):
            url = ("https://yandex.com.tr/search/?lr=11501&text={}={}".format(aranacak, x))
            istek = requests.get(url, headers=header)
            soup = BeautifulSoup(istek.content, "lxml")
            for i in soup.findAll("div", {"class": "organic"}):
                urls = i.a['href']
                print(urls)
                with open("dork.txt", "a") as f:
                    f.write(urls + "\n")
    except Exception as err:
        print(err)
