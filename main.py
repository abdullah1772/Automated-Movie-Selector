from bs4 import BeautifulSoup
import requests
import random


def main():  
    
    # URL you want to scrape data from
    URL = 'http://www.imdb.com/chart/top'
    
    #Get the html meta data using beautiful soup
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    #Extract key data elements from the html meta data
    movie_year = soup.select('td.titleColumn')

    movie_details = soup.select('td.titleColumn a')

    movie_rating = soup.select('td.posterColumn span[name=ir]')
    
    #Extract all the required values 

    #get a list of titles of all the movies
    title = []  
    for i in movie_details :
        title.append(i.text)

    #get a list of ratings of all the movies
    rating = []
    for i in movie_rating:
        rating.append(float(i['data-value']))
        
    #get a list of the years all the movies were released in
    year = []
    for i in movie_year :
        text = i.text.split()
        year.append(text[-1])
        
    #get a list of all the actors in the respective movies
    actor = []
    for i in movie_details:
        actor.append(i['title'])
        
        
    #get the total number of movies 
    no_of_movies = len(title)

    #Get a random value
    idx = random.randrange(0, no_of_movies)

    #print the details of the random picked movie
    print(title[idx], year[idx], "Rating:" , round(rating[idx],1), "Starring:" ,actor[idx])
    

if __name__ == '__main__':
    main()