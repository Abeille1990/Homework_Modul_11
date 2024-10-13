import requests

print('Please enter a keyword for film search (English) :')
keyword = str(input())
print('Enter release year(1960 to 2024):')
y = input()


ACCESS_TOKEN = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMTEyYjdjYzIxMzRjNjgzZTNjNjA5YTQyNWVjZjJlYiIsIm5iZiI6MTcyODgyNzYzNS44MDE4ODMsInN1YiI6IjY3MGJjYjJlMzdkODZkNTIwYmIwZWE2NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Kod83hWWmcid2yUxIkKnmkEDzx45vZedzqhiuxOzis0"
API_URL = 'https://api.themoviedb.org/3/search/movie'
TMDB_URL = 'https://www.themoviedb.org'

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMTEyYjdjYzIxMzRjNjgzZTNjNjA5YTQyNWVjZjJlYiIsIm5iZiI6MTcyO"
                     "DgyNzYzNS44MDE4ODMsInN1YiI6IjY3MGJjYjJlMzdkODZkNTIwYmIwZWE2NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZX"
                     "JzaW9uIjoxfQ.Kod83hWWmcid2yUxIkKnmkEDzx45vZedzqhiuxOzis0"
}


data = requests.get(API_URL, headers=headers, params={'query': keyword, 'language': 'en-US', 'year': y})
data = data.json()

source = data['results']

print()
for n in range(len(source)):
    info = f"{source[n]['title']}, {source[n]['release_date']}\nPopularity:{round(source[n]['popularity'],1)}"
    print(info)
    print()


