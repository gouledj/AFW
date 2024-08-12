from django.core.management.base import BaseCommand
from fires.models import WildfireReport
from django.utils import dateparse, timezone
import requests
from bs4 import BeautifulSoup
import re

class Command(BaseCommand):
    help = 'Scrape wildfire data and save to database'

    def handle(self, *args, **kwargs):
        def scrape_official_data():
            url = 'https://srd.web.alberta.ca/wildfires-of-note'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

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
                    date = dateparse.parse_date(date_str)
                    if not date:
                        date = timezone.now().date()
                else:
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

        # Execute the function
        save_wildfire_reports()
