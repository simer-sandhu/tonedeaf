
import requests, bs4
from bs4 import BeautifulSoup

#base url for the pages

base_url = "https://guitarpatches.com/patches.php?unit=Katana"
search_phrase = "Simer"
found = False

def check_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # searching for my previous name in text
        if search_phrase.lower() in soup.get_text().lower():
            return True
        return False

# there are like 30 pages so loop pages until found or out of pages
page = 1
while not found:
    url= f"{base_url}&sort=&page={page}"
    print(f"Checking {url}...")

    if check_page(url):
        print(f"Found '{search_phrase}' on page {page}: {url}")
        found = True
    else:
        page += 1
        #break loop for no more pages or condition
        if page > 34: # there are 15 for the mkii katana amp
            print("No Phrase here")
            break
if not found:
    print("phrase not found")

#found my tame impala tone on page 20 after having some issues with visualstudiocode terminal