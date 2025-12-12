import requests
from bs4 import BeautifulSoup
import csv
import re

def scrape_hotel(url, hotel_name):
    """Scrape hotel room data from the website"""
    try:
        print(f"\nScraping {hotel_name}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        rooms = []
        
        # Find all text content
        all_text = soup.get_text()
        lines = [line.strip() for line in all_text.split('\n') if line.strip()]
        
        # Pattern to find hotel names and prices
        for i, line in enumerate(lines):
            # Look for euro prices
            price_match = re.search(r'€\s*(\d+)', line)
            
            if price_match:
                price = '€ ' + price_match.group(1)
                
                # Find hotel name (usually 1-3 lines before price)
                hotel_title = ''
                for j in range(max(0, i-5), i):
                    if len(lines[j]) > 10 and len(lines[j]) < 100:
                        if not re.search(r'€\s*\d+', lines[j]):
                            if re.search(r'[A-Z]', lines[j]):
                                hotel_title = lines[j]
                                break
                
                if not hotel_title:
                    hotel_title = 'Unknown Hotel'
                
                # Find room type
                room_type = 'Standard Room'
                for j in range(max(0, i-3), min(len(lines), i+3)):
                    if re.search(r'(King|Queen|Double|Twin|Suite|Studio|Room|Bed)', lines[j], re.I):
                        if not re.search(r'€\s*\d+', lines[j]):
                            room_type = lines[j]
                            break
                
                rooms.append({
                    'Hotel': hotel_title[:60],
                    'Room_Type': room_type[:50],
                    'Price': price,
                    'Period': '20-30 December 2025'
                })
                
                if len(rooms) >= 40:
                    break
        
        print(f"Successfully scraped {len(rooms)} rooms from {hotel_name}")
        return rooms
        
    except Exception as e:
        print(f"Error scraping {hotel_name}: {e}")
        return []

def save_csv(data, filename='hotel_prices.csv'):
    """Save scraped data to CSV file"""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Hotel', 'Room_Type', 'Price', 'Period'])
            writer.writeheader()
            writer.writerows(data)
        print(f"\n" + "="*70)
        print(f"SUCCESS! CSV file created: {filename}")
        print(f"="*70)
        return True
    except Exception as e:
        print(f"Error saving CSV: {e}")
        return False

# MAIN EXECUTION
print("="*70)
print("HOTEL PRICE SCRAPER - December 20-30, 2025")
print("="*70)

# Target websites
hotels = [
    ('https://booking-hotels2.tiiny.site/', 'DublinStays'),
    ('https://hotel1.tiiny.site', 'Luxe Haven')
]

all_rooms = []

# Scrape each website
for url, name in hotels:
    rooms = scrape_hotel(url, name)
    all_rooms.extend(rooms)

# Save results to CSV
if all_rooms:
    save_csv(all_rooms)
    print(f"\nTotal rooms in CSV: {len(all_rooms)}")
    print(f"Period: 20-30 December 2025")
    print(f"\nYou can now open 'hotel_prices.csv' in Excel!")
    print("="*70)
else:
    print("\nNo data scraped! Check your internet connection.")