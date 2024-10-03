import tkinter as tk
from tkinter import messagebox, ttk

# Structure to hold flight information
class Flight:
    def __init__(self, flight_number, departure, arrival, departure_time, arrival_time, gate, crew_id):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.gate = gate
        self.crew_id = crew_id

flights = []  # List to store flight objects

# Function to handle submission of flight details
def submit_flight():
    flight_number = entry_flight_number.get()
    departure = entry_departure.get()
    arrival = entry_arrival.get()
    departure_time = entry_departure_time.get()
    arrival_time = entry_arrival_time.get()
    gate = entry_gate.get()
    crew_id = entry_crew_id.get()

    if flight_number and departure and arrival and departure_time and arrival_time and gate and crew_id:
        # Create a new flight object and add it to the flights list
        flight = Flight(flight_number, departure, arrival, departure_time, arrival_time, gate, crew_id)
        flights.append(flight)
        messagebox.showinfo("Success", f"Flight {flight_number} has been added to the schedule.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill all the fields.")

# Function to clear input fields after submission
def clear_entries():
    entry_flight_number.delete(0, tk.END)
    entry_departure.delete(0, tk.END)
    entry_arrival.delete(0, tk.END)
    entry_departure_time.delete(0, tk.END)
    entry_arrival_time.delete(0, tk.END)
    entry_gate.delete(0, tk.END)
    entry_crew_id.delete(0, tk.END)

# Function to perform First Come First Serve (FCFS) scheduling
def fcfs_schedule():
    if not flights:
        messagebox.showwarning("No Flights", "No flights have been added yet.")
        return

    sorted_flights = sorted(flights, key=lambda flight: flight.departure_time)
    schedule_window = tk.Toplevel(root)
    schedule_window.title("FCFS Schedule")

    text = tk.Text(schedule_window)
    text.pack()

    text.insert(tk.END, "--- First Come First Serve (FCFS) Schedule ---\n\n")
    for flight in sorted_flights:
        flight_info = f"Flight {flight.flight_number}: Departure {flight.departure} at {flight.departure_time}, Arrival {flight.arrival} at {flight.arrival_time}, Gate {flight.gate}, Crew ID {flight.crew_id}\n"
        text.insert(tk.END, flight_info)

# Function to perform Priority Scheduling (based on gate availability)
def priority_schedule():
    if not flights:
        messagebox.showwarning("No Flights", "No flights have been added yet.")
        return

    sorted_flights = sorted(flights, key=lambda flight: int(flight.gate))
    schedule_window = tk.Toplevel(root)
    schedule_window.title("Priority Schedule")

    text = tk.Text(schedule_window)
    text.pack()

    text.insert(tk.END, "--- Priority Scheduling (by Gate) ---\n\n")
    for flight in sorted_flights:
        flight_info = f"Flight {flight.flight_number}: Departure {flight.departure} at {flight.departure_time}, Arrival {flight.arrival} at {flight.arrival_time}, Gate {flight.gate}, Crew ID {flight.crew_id}\n"
        text.insert(tk.END, flight_info)

# Setting up the main window
root = tk.Tk()
root.title("Airline Scheduling System")
root.geometry("400x400")

# Labels and Entry Fields for Flight Details
tk.Label(root, text="Flight Number:").grid(row=0, column=0, padx=10, pady=5)
entry_flight_number = tk.Entry(root)
entry_flight_number.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Departure:").grid(row=1, column=0, padx=10, pady=5)
entry_departure = tk.Entry(root)
entry_departure.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Arrival:").grid(row=2, column=0, padx=10, pady=5)
entry_arrival = tk.Entry(root)
entry_arrival.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Departure Time:").grid(row=3, column=0, padx=10, pady=5)
entry_departure_time = tk.Entry(root)
entry_departure_time.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Arrival Time:").grid(row=4, column=0, padx=10, pady=5)
entry_arrival_time = tk.Entry(root)
entry_arrival_time.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Gate:").grid(row=5, column=0, padx=10, pady=5)
entry_gate = tk.Entry(root)
entry_gate.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Crew ID:").grid(row=6, column=0, padx=10, pady=5)
entry_crew_id = tk.Entry(root)
entry_crew_id.grid(row=6, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit Flight", command=submit_flight)
submit_button.grid(row=7, column=0, columnspan=2, pady=10)

# FCFS and Priority Scheduling Buttons
fcfs_button = tk.Button(root, text="FCFS Schedule", command=fcfs_schedule)
fcfs_button.grid(row=8, column=0, columnspan=2, pady=10)

priority_button = tk.Button(root, text="Priority Schedule", command=priority_schedule)
priority_button.grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()
