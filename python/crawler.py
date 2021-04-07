import codecs
f = codecs.open("index.html", 'r', 'shift-jis')
from bs4 import BeautifulSoup


contents = f.read()

soup = BeautifulSoup(contents, 'lxml')

link_list = soup.find_all(href=True)


link_list

from pathlib import Path
import requests
filename = Path('metadata.pdf')
url = 'http://www.hrecos.org//images/Data/forweb/HRTVBSH.Metadata.pdf'
response = requests.get(url)
filename.write_bytes(response.content)

