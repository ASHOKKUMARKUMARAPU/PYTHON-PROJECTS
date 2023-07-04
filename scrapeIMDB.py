from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top Rated Movies'
#print(excel.sheetnames)

sheet.append(['Movie Rank','Movie Name','Year of Release','IMDB Rating'])

try:
    URL = 'https://www.imdb.com/chart/top/'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content,'html.parser')

    #print(soup)

    movies = soup.find('tbody', class_="lister-list").find_all('tr')

    #print(movies)
    #print(len(movies))

    for movie in movies:
        name = movie.find('td',class_='titleColumn').a.text
        
        rank = movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
        
        year = movie.find('td',class_='titleColumn').span.text.strip('()')
        
        rating = movie.find('td',class_='ratingColumn imdbRating').strong.text
        
        print(rank, name, year, rating)
        sheet.append([rank, name, year, rating])
    
except Exception as e:
    print(e)
    
excel.save('IMDB Movie Ratings.xlsx')







