import unittest
from amazon_scraper import AmazonItem, parse_amazon_html

class TestAmazonScraper(unittest.TestCase):
    def test_parse_amazon_html(self):
        with open('amazon.html', 'r') as f:
            html_content = f.read()
        items = parse_amazon_html(html_content)
        self.assertEqual(len(items), 3)
        self.assertEqual(items[0].name, 'Sample Item 1')
        self.assertEqual(items[0].price, '$19.99')
        self.assertEqual(items[1].name, 'Sample Item 2')
        self.assertEqual(items[1].price, '$24.99')
        self.assertEqual(items[2].name, 'Sample Item 3')
        self.assertEqual(items[2].price, '$14.99')

if __name__ == '__main__':
    unittest.main()