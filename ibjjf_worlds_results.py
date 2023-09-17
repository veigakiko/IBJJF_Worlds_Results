# -*- coding: utf-8 -*-
"""IBJJF_Worlds_Results.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x8cLV92A4kyT6zw-EAfLpydkidyt2knq

### **Previsão de Campeões Mundiais** de *Jiu-Jitsu* em 2024 com **Machine Learning**
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

url = 'https://www.ibjjfdb.com/ChampionshipResults/2025/PublicResults'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.title.get_text().strip()
elements = soup.find_all(['div', 'h4'], class_=['athlete-item', 'subtitle', 'position-athlete'])
championships = [elem.get_text().strip() for elem in elements if elem['class'] == ['athlete-item']]
categories = [elem.get_text().strip() for elem in elements if elem['class'] == ['subtitle']]
position = [elem.get_text().strip() for elem in elements if elem['class'] == ['position-athlete']]
data = {'title': title, 'categories': categories,'championships': championships,'position': position}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
with open('data.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f)

resultsdf = []
for t in range(0,len(json_file['championships'])):
    athlete_name =  ((json_file['championships'][t][52:][:80])).strip()
    academie_name = ((json_file['championships'][t][200:])).strip()
    position_name = json_file['position'][t]
    categories_name = json_file['categories'][3]
    resultsdf.append((position_name, athlete_name, academie_name, categories_name))

df = pd.DataFrame(resultsdf, columns=['Results','Name','Academy','Category'])
df.head(2)

df.shape

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

# Define the URL
url = 'https://www.ibjjfdb.com/ChampionshipResults/2025/PublicResults'

# Send an HTTP GET request
response = requests.get(url)
response.raise_for_status()  # Raise an error if the request fails

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract title
title = soup.title.get_text().strip()

# Find all relevant elements
elements = soup.find_all(['div', 'h4'], class_=['athlete-item', 'subtitle', 'position-athlete'])

# Initialize lists to store data
championships = []
categories = []
position = []

# Extract data into lists
for elem in elements:
    if 'athlete-item' in elem['class']:
        championships.append(elem.get_text().strip())
    elif 'subtitle' in elem['class']:
        categories.append(elem.get_text().strip())
    elif 'position-athlete' in elem['class']:
        position.append(elem.get_text().strip())

# Create a dictionary to store the data
data = {'title': title, 'categories': categories, 'championships': championships, 'position': position}

# Save the data to a JSON file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# Read the data from the JSON file
with open('data.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f)

# Create a list of tuples for DataFrame construction
resultsdf = [(pos, champ[52:][:80].strip(), champ[200:].strip(), cat) for pos, champ, cat in zip(json_file['position'], json_file['championships'], json_file['categories'])]

# Create a DataFrame from the list of tuples
df = pd.DataFrame(resultsdf, columns=['Results', 'Name', 'Academy', 'Category'])
df.head(10)



import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

# Define the URL of the website to scrape
url = 'https://www.ibjjfdb.com/ChampionshipResults/2025/PublicResults'

# Send an HTTP GET request to the URL and check for errors
response = requests.get(url)
response.raise_for_status()

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the title of the website
title = soup.title.get_text().strip()

# Find all the elements that contain the relevant data
elements = soup.find_all(['div', 'h4'], class_=['athlete-item', 'subtitle', 'position-athlete'])

# Initialize empty lists to store the data
championships, categories, position = [], [], []

# Loop through the elements and extract the data into the lists
for elem in elements:
    class_name = elem['class'][0] if elem['class'] else None
    text = elem.get_text().strip()

    if class_name == 'athlete-item':
        championships.append(text)
    elif class_name == 'subtitle':
        categories.append(text)
    elif class_name == 'position-athlete':
        position.append(text)

categories

championships

position

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

# Define the URL of the website to scrape
url = 'https://www.ibjjfdb.com/ChampionshipResults/2025/PublicResults'

# Send an HTTP GET request to the URL and check for errors
response = requests.get(url)
response.raise_for_status()

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the title of the website
title = soup.title.get_text().strip()

# Find all the elements that contain the relevant data
elements = soup.find_all(['div', 'h4'], class_=['athlete-item', 'subtitle', 'position-athlete'])

# Initialize empty lists to store the data
championships, categories, position = [], [], []

# Loop through the elements and extract the data into the lists
for elem in elements:
    class_name = elem['class'][0] if elem['class'] else None
    text = elem.get_text().strip()

    if class_name == 'athlete-item':
        championships.append(text)
    elif class_name == 'subtitle':
        categories.append(text)
    elif class_name == 'position-athlete':
        position.append(text)

# Create a dictionary to store the data with keys and values
data = {'title': title, 'categories': categories, 'championships': championships, 'position': position}

# Save the data to a JSON file with UTF-8 encoding and indentation
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# Read the data from the JSON file with UTF-8 encoding
with open('data.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f)

# Create a list of tuples for DataFrame construction by slicing and formatting the strings
resultsdf = [(pos, champ[52:][:80].strip(), champ[200:].strip(), cat) for pos, champ, cat in zip(json_file['position'], json_file['championships'], json_file['categories'])]

# Create a DataFrame from the list of tuples with column names
df = pd.DataFrame(resultsdf, columns=['Results', 'Name', 'Academy', 'Category'])
df