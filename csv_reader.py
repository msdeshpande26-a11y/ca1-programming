import csv
from pathlib import Path

def display_csv(filename='hotel_prices.csv'):
    """Read and display CSV data"""
    try:
        if not Path(filename).exists():
            print(f"Error: {filename} not found!")
            return False
        
        print("\n" + "=" * 80)
        print("HOTEL ROOM PRICE COMPARISON")
        print("=" * 80)
        
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        if not rows:
            print("No data found!")
            return False
        
        # Display table
        print("\n{:<25} {:<30} {:<15} {:<20}".format("Hotel", "Room Type", "Price", "Period"))
        print("-" * 90)
        
        for row in rows:
            print("{:<25} {:<30} {:<15} {:<20}".format(
                row['Hotel'][:25], 
                row['Room_Type'][:30], 
                row['Price'][:15], 
                row['Period'][:20]
            ))
        
        # Summary
        print("\n" + "=" * 80)
        print(f"Total rooms: {len(rows)}")
        
        # Count by hotel
        hotels = {}
        for row in rows:
            hotels[row['Hotel']] = hotels.get(row['Hotel'], 0) + 1
        
        print("\nBy hotel:")
        for hotel, count in hotels.items():
            print(f"  {hotel}: {count} rooms")
        
        print("=" * 80 + "\n")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

# Main execution
display_csv()