import requests
from bs4 import BeautifulSoup

class AmazonItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def parse_amazon_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    items = []
    for item_div in soup.find_all('div', class_='item'):
        name_span = item_div.find('span', class_='a-size-medium')
        price_span = item_div.find('span', class_='a-price')
        if name_span and price_span:
            items.append(AmazonItem(name_span.text, price_span.text))
    return items

def scrape_amazon(url):
    response = requests.get(url)
    return parse_amazon_html(response.content)

if __name__ == '__main__':
    url = 'amazon.html'  # replace with your URL
    items = scrape_amazon(url)
    for item in items:
        print(f"Name: {item.name}, Price: {item.price}")