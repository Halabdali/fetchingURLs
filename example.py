# intellectual property belongs to imdb    
import urllib.request
from bs4 import BeautifulSoup

# get the SOUP: tree structure out of the HTML page
soup = BeautifulSoup(urllib.request.urlopen("http://www.imdb.com/title/tt0413573/episodes?season=10"))

result = {}
for div in soup.find_all("div", {"class":"airdate"}):
    # get the date and number and store in a dictionary
    date = div.text.encode('utf-8').strip()
    number = div.find_previous_sibling()['content']
    result[number] = date
print(result)