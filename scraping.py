import requests
from bs4 import BeautifulSoup

# Step 1: Choose a news site 
URL = "https://www.bbc.com/news"

# Step 2: Fetch HTML content
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

# Step 3: Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract headlines (BBC uses <h2> tags for many headlines)
headlines = []
for h2 in soup.find_all("h2"):
    text = h2.get_text(strip=True)
    if text and text not in headlines:  # avoid duplicates
        headlines.append(text)

# Step 5: Save headlines to a text file
with open("headlines.txt", "w", encoding="utf-8") as f:
    for idx, headline in enumerate(headlines, 1):
        f.write(f"{idx}. {headline}\n")

print(f" Scraping complete! {len(headlines)} headlines saved to headlines.txt")
