import requests
import pandas as pd

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

params = (
    ('ResultOrder', 'Popularity'),
    ('CountryCode', 'RU'),
    ('subjectId', '13'),
)

response = requests.get('https://www.ebooks.com/api/search/subject/', headers=headers, params=params)

results_json = response.json()['books']

title = []
subtitle = []
author = []
publisher = []
publication_year = []
price = []

for result in results_json:
    # title
    title.append(result['title'])
    
    # subtitle
    subtitle.append(result['subtitle'])
    
    # author
    author.append(result['authors'][0]['author_name'])
    
    # publisher
    publisher.append(result['publisher'])
    
    # publication year
    publication_year.append(result['publication_year'])
    
    # price
    price.append(result['price'])

books_df = pd.DataFrame({'Title': title, 'Subtitle': subtitle, 'Author': author, 'Publisher': publisher,
                         'Publication Year': publication_year, 'Price': price})
books_df.to_excel('books.xlsx', index=False)


