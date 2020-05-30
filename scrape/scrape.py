import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
#print (response.text) <-- Print the HTML I received from the request

soup = BeautifulSoup(response.text,'html.parser')

#print(soup.find_all('div'))  <-- I get all the DIV
#print(soup.find_all('a')) #  <-- I get all the links
#print(soup.select('.score')) #  <-- I get all the scores and spam

links = soup.select('.storylink') #  <-- I get the titles by the CSS class storylink. See the HTML
subtext = soup.select('.subtext') #  <-- I get the scores in a list by the CSS class subtext. See the HTML
#votes = soup.select('.score') #  <-- BAD IDEA, the score might not exist. We will get a higher element, subtext. I get the scores in a list by the CSS class score. See the HTML

def sort_stories_by_votes(hn):
    return sorted(hn, key = lambda k:k['votes'], reverse = True)

def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText() # <--  getting each title
        href = links[index].get('href', None) # <--  getting the URL Link
        vote = subtext[index].select('.score') # <-- Now I get the score, and I check if it exists
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            #print(points)
            if points > 99:
                hn.append({'title':title, 'link':href, 'votes':points})
                
        #print(title) 
        #print(href) 
    return hn

hn = create_custom_hn(links, subtext)
hn = sort_stories_by_votes(hn)
pprint.pprint(hn)
