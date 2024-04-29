from bs4 import BeautifulSoup
import requests

# def examine_example_page():
#     req = requests.get("http://www.example.com/").test
#     soup = BeautifulSoup(req, "html.parser")
#     return soup

# example_contet = examine_example_page()


#def get_html_content():
 #   soup = BeautifulSoup(open("index.html"), "html.parser")
  #  return soup.prettify()


#content = get_html_content()
#soup = BeautifulSoup(content, "html.parser")

#a_tag = soup.a
#print(a_tag.name)
#print(a_tag.attrs)
#print(a_tag.string)

def get_pigs_html():
    soup = BeautifulSoup(open("index.html"), "html.parser")
    return soup

#print(get_pigs_html().p)
pig_soup = get_pigs_html()

# p_tag = pig_soup.body.a.next_siblings

p_tag = pig_soup.body.p.next_sibling.next_sibling

for child in p_tag.childern:
    if hasattr(child, "attrs") and "href" in child.attrs:
      print(child.attrs)
      print(child.attrs["href"])


print(pig_soup.find(name="a"))


print(pig_soup.find_all(class_="pig"))

#print(pig_soup.find(attrs=("class": "pig", "href": True)))

pig_soup.find(strings="Mo")

# a_tags = get_pigs_html().a
# print([p.name for p in a_tags.parents])

# tags = list(a_tags.next_siblings)
# print(tags)