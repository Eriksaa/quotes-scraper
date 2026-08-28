import requests
from bs4 import BeautifulSoup
import csv

base_url = 'http://quotes.toscrape.com/page/{}/'
all_data = []

# Loop dari halaman 1 sampai 10
for page in range(1, 11):
    response = requests.get(base_url.format(page))
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quote_blocks = soup.find_all('div', class_='quote')
    
    for block in quote_blocks:
        text = block.find('span', class_='text').text
        author = block.find('small', class_='author').text
        tags = [tag.text for tag in block.find_all('a', class_='tag')]
        
        all_data.append({
            'author': author, 
            'quote': text, 
            'tags': ", ".join(tags)
        })
    
    print(f"Halaman {page} berhasil ditarik!")

# Menyimpan hasil ke dataset CSV
with open('quotes_dataset.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['author', 'quote', 'tags'])
    writer.writeheader()
    writer.writerows(all_data)

print("Scraping selesai! File quotes_dataset.csv berhasil dibuat.")