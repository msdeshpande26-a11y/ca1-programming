import csv
from pathlib import Path

def display_csv(filename='hotel_prices.csv'):
    """Read and display CSV data with improved formatting"""
    try:
        if not Path(filename).exists():
            print(f"Error: {filename} not found!")
            print(f"Please run hotel_scraper.py first to generate the CSV file.")
            return False
        
        print("\n" + "=" * 90)
        print("         HOTEL ROOM PRICE COMPARISON - December 20-30, 2025")
        print("=" * 90)
        
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        if not rows:
            print("No data found in CSV!")
            return False
        
        # Display table header
        print("\n{:<35} {:<30} {:<15} {:<25}".format(
            "HOTEL", "ROOM TYPE", "PRICE", "PERIOD"
        ))
        print("-" * 105)
        
        # Display each row
        for i, row in enumerate(rows, 1):
            print("{:<35} {:<30} {:<15} {:<25}".format(
                row['Hotel'][:34], 
                row['Room_Type'][:29], 
                row['Price'][:14], 
                row['Period'][:24]
            ))
        
        # Summary statistics
        print("\n" + "=" * 90)
        print(f"SUMMARY:")
        print(f"   Total rooms listed: {len(rows)}")
        
        # Count by hotel/source
        hotels = {}
        for row in rows:
            hotel_key = row['Hotel']
            hotels[hotel_key] = hotels.get(hotel_key, 0) + 1
        
        print(f"   Unique hotels: {len(hotels)}")
        
        # Show breakdown
        print(f"\n   Breakdown by source:")
        hotel_counts = sorted(hotels.items(), key=lambda x: x[1], reverse=True)
        for hotel, count in hotel_counts[:10]:  # Show top 10
            print(f"      - {hotel[:40]}: {count} rooms")
        
        if len(hotel_counts) > 10:
            print(f"      ... and {len(hotel_counts) - 10} more hotels")
        
        # Price analysis (extract numeric values)
        prices = []
        for row in rows:
            price_str = row['Price']
            # Extract numbers from price string
            import re
            price_match = re.search(r'(\d+)', price_str.replace(',', ''))
            if price_match:
                prices.append(int(price_match.group(1)))
        
        if prices:
            print(f"\n   Price Range:")
            print(f"      - Minimum: EUR {min(prices)}")
            print(f"      - Maximum: EUR {max(prices)}")
            print(f"      - Average: EUR {sum(prices)//len(prices)}")
        
        print("=" * 90 + "\n")
        return True
        
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return False

# Main execution
if __name__ == "__main__":
    display_csv()