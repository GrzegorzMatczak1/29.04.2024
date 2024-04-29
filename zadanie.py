from bs4 import BeautifulSoup
import requests

# def examine_example_page():
#     req = requests.get("http://www.example.com/").text
#     soup = BeautifulSoup(req, 'html.parser')
#     return soup

# example_contet = examine_example_page()

# def get_html_content():
#     soup = BeautifulSoup(open('index.html'), 'html.parser')
#     return soup.prettify()


# content = get_html_content()
# soup = BeautifulSoup(content, 'html.parser')

# a_tag = soup.a
# print(a_tag.name)
# print(a_tag.attrs)
# print(a_tag.string)



# get pigs.html content
def get_pigs_html():
    req = requests.get("https://pogoda.interia.pl/prognoza-dlugoterminowa-zgierz,cId,41420").text
    soup = BeautifulSoup(req, 'html.parser')
    return soup

# invoke method and store it inside variable
pig_soup = get_pigs_html()

# get 2nd p tag
p_tag = pig_soup.body.p.next_sibling.next_sibling


# iterate over children of 2nd p tag
for child in p_tag.children:
    if hasattr(child, "attrs") and "href" in child.attrs:
        print(child.attrs) # prints all attributes
        print(child.attrs["href"]) # print href attribute

# a_tags = get_pigs_html().a
# print([p.name for p in a_tags.parents])

# tags = list(a_tags.next_siblings)
# print(tags)

# gets first a tag
# print("-----------------")
# print(pig_soup.find(name="a"))

# gets all tags with class pig
# print("-----------------")
# print(pig_soup.find_all(class_="pig"))

# gets tag with class pig and href attribute
# print("-----------------")
# print(pig_soup.find(attrs={"class": "pig", "href": "http://example.com/mo"}))

# gets tag which text contains Mo
#pig_soup.find(string='Mo')

print("-----------------")
print("Aktualna temp:", end=" ")
print(pig_soup.find(class_="weather-currently-temp-strict").string)
print("-----------------")

print("-----------------")
print("Odczuwalna temp:", end=" ")
print(pig_soup.find(class_="weather-currently-details").next_element.next_element.next_sibling.string)
print("-----------------")

print("-----------------")
print("Ciśnienie:", end=" ")
print(pig_soup.find(class_="pressure").next_sibling.next_sibling.string)
print("-----------------")

print("-----------------")
print("Wiatr:", end=" ")
print(pig_soup.find(class_="weather-currently-details-item wind").next_sibling.next_sibling)
print("-----------------")
