import requests
from bs4 import BeautifulSoup
import pprint

# Send HTTP requests to get the content of the first and second pages of the news site
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# Parse the HTML content of the pages using BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# Extract links and subtext information from the parsed HTML
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

# Combine links and subtext from both pages
mega_links = links + links2
mega_subtext = subtext + subtext2

# Function to sort the list of news stories by the number of votes in descending order
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

# Function to create a custom list of news stories with titles, links, and votes
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            # Extract the number of votes and convert it to an integer
            points = int(vote[0].getText().replace(' points', ''))
            # Only consider stories with more than 99 votes
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

# Print the sorted list of custom news stories
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
