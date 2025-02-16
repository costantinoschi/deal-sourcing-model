 # Web scraping script
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_crunchbase():
    url = "https://www.crunchbase.com/search/organizations/field/organization/num_funding_rounds"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    companies = []
    for company in soup.find_all('div', class_='company-name'):
        name = company.text.strip()
        companies.append({'Company': name})

    df = pd.DataFrame(companies)
    df.to_csv('data/companies.csv', index=False)
    print("Data saved to data/companies.csv")

if __name__ == "__main__":
    scrape_crunchbase()