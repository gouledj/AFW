# fires/scraping.py

import requests
from bs4 import BeautifulSoup
from .models import FireReport

def scrape_official_data():
    url = 'https://www.alberta.ca/wildfire-status.aspx'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Parse the HTML and extract information
    # This is just an example, you need to adjust according to the actual website structure
    reports = soup.find_all('div', class_='report')
    for report in reports:
        location = report.find('h2').text
        description = report.find('p').text
        FireReport.objects.create(
            source='Alberta Government',
            location=location,
            description=description,
            verified=True
        )
