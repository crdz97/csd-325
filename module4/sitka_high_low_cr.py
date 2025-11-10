import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:  
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {row[2]}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
print("Welcome to the Sitka Weather App!")
print("You can view the following:")
print(" H- High Temperatures")
print(" L- Low Temperatures")
print(" E- Exit the App")

#Main
while True:
    choice = input("\nEnter your choice (H/L/E): ").strip().lower()
 #Plot the high temperatures.
    if choice == 'h':
        print("Displaying high temperatures...")
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
    elif choice == 'l':
        print("Displaying low temperatures...")
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
    elif choice == 'e':
        print("Exiting the Sitka Weather App. Goodbye!")
        sys.exit()
    else: 
        print("Invalid choice. Please enter 'H', 'L', or 'E'.")   