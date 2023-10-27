from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())
# print(soup.title.name)
# print(soup.title.string)

# print(soup.title.parent)
# print(soup.title.parent.name)


# print(soup.p)

# print(soup.a)
# print(soup.find_all('a'))

# for link in soup.find_all('a'):
#     print(link.get('href'))


# print(soup.get_text())

# company_url = soup.select_one(selector=" p a")
# print(company_url)


# name = soup.select_one(selector="#name")
# print(name)

heading = soup.select(".heading")
print(heading)