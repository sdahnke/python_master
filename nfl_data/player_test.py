from robobrowser.browser import RoboBrowser
from bs4 import BeautifulSoup
import re

url = "http://www.footballdb.com/players/victor-abiamiri-abiamvi01"

br = RoboBrowser(history=False)

def playerstat(url)
    br.open(url)
    soup = BeautifulSoup(str(br.select), "html.parser")
    position = soup.find(text="Position:")
    college = soup.find(text="College:")



print(position.next)

print(college.next)