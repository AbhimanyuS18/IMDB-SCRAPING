
from bs4 import BeautifulSoup
import requests

def scrap_top_list():
    url='https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in'
    response=requests.get(url)

    soup=BeautifulSoup(response.text,'html.parser')
    movie_name=[]
    year_of_releas=[]
    movie_urls=[]
    movie_rating=[]
    movie_list = []

    tbody = soup.find("tbody", class_="lister-list")
    trs = tbody.find_all("tr")

    for tr in trs:
        # extracting movie names
        name = tr.find("td", class_="titleColumn")
        movie_name.append(name.a.get_text())

        # extracting movie year of release
        year = name.span.get_text()
        year_of_releas.append(int(year[1:-1]))
        
        # extracting movie link 
        url = name.a['href']
        movie_urls.append("https://www.imdb.com"+url)
        
        # extracting movie ratings
        ratings = tr.find("td", class_="ratingColumn imdbRating").get_text()
        movie_rating.append(float(ratings.strip()))

    for i in range(len(movie_name)):
        movie_list.append({
            "rank":i+1,
            "name":movie_name[i],
            "year":year_of_releas[i],
            "url":movie_urls[i],
            "rating":movie_rating[i]
        })
    return movie_list
        
from pprint import pprint 
pprint(scrap_top_list())

import json
with open('imdb_movies.json',"w") as a:
    json.dump(scrap_top_list(),a,indent=4)
