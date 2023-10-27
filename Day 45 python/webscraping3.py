# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
# movie_web_page = response.text

# soup = BeautifulSoup(movie_web_page , "html.parser")

 
# movie_title = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

# movie_titles = [movie.getText() for movie in movie_title]
# movies = movie_titles[::-1]
# print(movies)

# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")
x=[1,2,3,4,5]
print(x[0:-2:-4])