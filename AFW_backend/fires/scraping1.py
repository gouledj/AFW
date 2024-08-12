import requests
from bs4 import BeautifulSoup
from myapp.models import WildfireReport
import re
from django.utils.date_parse import parse_date
from django.utils import timezone

def scrape_official_data():
    url = 'https://srd.web.alberta.ca/wildfires-of-note'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant information
    wildfires_info = []

    for item in soup.find_all('div', class_='post-item'):
        date_str = item.find('h2').get_text(strip=True)
        summary = item.find('p', style='font-size: 12px;').get_text(strip=True)
        description = item.find('div', class_='post-body clearfix')

        paragraphs = []
        if description:
            for p in description.find_all('p'):
                paragraphs.append(p.get_text(strip=True))

        details = "\n".join(paragraphs)

        # Convert date string to a Django-compatible date
        date_match = re.search(r'\w+ \d{1,2}, \d{4}', date_str)
        if date_match:
            date_str = date_match.group(0)
            date = parse_date(date_str)
            if not date:
                # If parsing fails, use today's date as fallback
                date = timezone.now().date()
        else:
            # If date format is incorrect, use today's date
            date = timezone.now().date()

        wildfires_info.append({
            'date': date,
            'summary': summary,
            'details': details
        })

    return wildfires_info

def save_wildfire_reports():
    wildfires_info = scrape_official_data()

    for info in wildfires_info:
        WildfireReport.objects.update_or_create(
            date=info['date'],
            defaults={
                'summary': info['summary'],
                'details': info['details']
            }
        )

# Example usage
if __name__ == "__main__":
    save_wildfire_reports()
