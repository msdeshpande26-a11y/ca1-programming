import requests
from bs4 import BeautifulSoup
import csv
import re

def scrape_hotel(url, hotel_name):
    """Scrape hotel room data"""
    try:
        print(f"\nScraping {hotel_name}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        rooms = []
        
        # Strategy 1: Look for table rows
        table_rows = soup.find_all('tr')
        if len(table_rows) > 1:
            for row in table_rows[1:]:  # Skip header
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 2:
                    try:
                        rooms.append({
                            'Hotel': hotel_name,
                            'Room_Type': cells[0].get_text(strip=True),
                            'Price': cells[1].get_text(strip=True),
                            'Period': '20-30 December 2024'
                        })
                    except:
                        continue
        
        # Strategy 2: Look for divs/articles with class containing 'room' or 'card'
        if not rooms:
            room_divs = soup.find_all(['div', 'article'], class_=re.compile(r'room|card|item|product', re.I))
            for div in room_divs[:15]:
                try:
                    name = div.find(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'span'])
                    price_elem = div.find(string=re.compile(r'[\$€£]\s*\d+|price', re.I))
                    
                    if name and price_elem:
                        rooms.append({
                            'Hotel': hotel_name,
                            'Room_Type': name.get_text(strip=True),
                            'Price': price_elem.strip(),
                            'Period': '20-30 December 2024'
                        })
                except:
                    continue
        
        # Strategy 3: Search all text for price patterns
        if not rooms:
            all_text = soup.get_text()
            lines = [line.strip() for line in all_text.split('\n') if line.strip()]
            
            for i, line in enumerate(lines):
                if re.search(r'[\$€£]\s*\d+', line):
                    # Look for room name in previous or same line
                    room_name = lines[i-1] if i > 0 and not re.search(r'[\$€£]\s*\d+', lines[i-1]) else line.split('$')[0].strip()
                    if room_name and len(room_name) > 2:
                        rooms.append({
                            'Hotel': hotel_name,
                            'Room_Type': room_name[:50],
                            'Price': line,
                            'Period': '20-30 December 2024'
                        })
                        if len(rooms) >= 10:
                            break
        
        print(f"Found {len(rooms)} rooms")
        return rooms[:15]  # Limit to 15 rooms
        
    except Exception as e:
        print(f"Error scraping {hotel_name}: {e}")
        return []

def save_csv(data, filename='hotel_prices.csv'):
    """Save data to CSV"""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Hotel', 'Room_Type', 'Price', 'Period'])
            writer.writeheader()
            writer.writerows(data)
        print(f"\nSaved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving: {e}")
        return False

# Main execution
print("=" * 50)
print("Hotel Price Scraper")
print("=" * 50)

hotels = [
    ('https://booking-hotels2.tiiny.site/', 'Booking Hotels 2'),
    ('https://hotel1.tiiny.site', 'Hotel 1')
]

all_rooms = []
for url, name in hotels:
    all_rooms.extend(scrape_hotel(url, name))

if all_rooms:
    save_csv(all_rooms)
    print(f"\nTotal rooms: {len(all_rooms)}")
else:
    print("\nNo data scraped! Please check if websites are accessible.")