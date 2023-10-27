from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")


articles = soup.find_all("a", class_="hnuser")


article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get("href")
    
    
    article_texts.append(text)
    article_links.append(link)


score_point = soup.find_all(name ="span", class_="score")
article_upvote = [ score.getText().split()[0] for score in score_point] 

# print(article_texts)
# print(article_links)
# print(article_upvote)

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

