import requests
import string
from collections import Counter
from bs4 import BeautifulSoup
#url = "https://bbc.com/news"
url = "https://realpython.com/community/"

all_nouns = []
print("Fetching {}".format(url))
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

words = soup.text.split()
nouns = [word for word in words if word.isalpha() and word[0] in string.ascii_uppercase]
all_nouns += nouns
print(Counter(all_nouns).most_common(100))