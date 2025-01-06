import tkinter as tk
import pytz
from datetime import datetime

# Function to get the current time and date in IST
def get_time_in_ist():
    # Define IST timezone
    india_timezone = pytz.timezone("Asia/Kolkata")
    # Get the current time in UTC and convert it to IST
    utc_time = datetime.now(pytz.utc)
    ist_time = utc_time.astimezone(india_timezone)
    
    # Format the time and date
    current_time = ist_time.strftime("%H:%M:%S")  # Time in HH:MM:SS format
    current_date = ist_time.strftime("%d-%m-%Y")  # Date in DD-MM-YYYY format
    return current_time, current_date

# Function to update the clock on the GUI
def update_clock():
    current_time, current_date = get_time_in_ist()

    # Update the labels with the current time and date
    time_label.config(text=current_time)
    date_label.config(text=current_date)

    # Call the update_clock function every 1000 milliseconds (1 second)
    root.after(1000, update_clock)

# Set up the tkinter window
root = tk.Tk()
root.title("Clock in IST")

# Create labels to display the time and date
time_label = tk.Label(root, font=("Arial", 50), fg="black")
time_label.pack()

date_label = tk.Label(root, font=("Arial", 25), fg="black")
date_label.pack()

# Start updating the clock
update_clock()

# Run the tkinter event loop
root.mainloop()
