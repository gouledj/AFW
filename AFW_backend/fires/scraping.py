import requests
from bs4 import BeautifulSoup

def scrape_official_data():
    url = 'https://srd.web.alberta.ca/wildfires-of-note'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant information
    wildfires_info = []

    # Adjust the parsing logic based on the actual HTML structure of the page
    # For this example, I'm assuming each wildfire info is contained within a specific tag
    for item in soup.find_all('div', class_='post-item'):  # Adjust the tag and class based on the actual structure
        wildfire = {}
        # print(item)

    
        # Extract the date
        date = item.find('h2')
        if date:
            wildfire['date'] = date.get_text(strip=True)

        print(date.get_text(strip=True))

                # numberofWildfires = description.find('p')

        # print(numberofWildfires.get_text(strip=True))

        # Extract the description or other details
        description = item.find('div', class_='post-body clearfix')  # Replace with actual class name if different


        if description:
            
            for p in description.find_all('p'):
                print(p.get_text(strip=True))
                
                
            
            
            # wildfire['description'] = description.get_text(strip=True)

        wildfires_info.append(wildfire)

        # print(description)

    return wildfires_info

# Example usage
wildfires_info = scrape_official_data()

# Print the extracted information
# for info in wildfires_info:
#     print(f"Title: {info.get('title', 'N/A')}")
#     print(f"Date: {info.get('date', 'N/A')}")
#     print(f"Description: {info.get('description', 'N/A')}")
#     print('-' * 40)
