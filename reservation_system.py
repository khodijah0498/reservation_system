import csv


tables =[
{
    'number': 1, 'seats': 2
},
{
    'number': 2, 'seats': 6
},
{
    'number': 3, 'seats': 2
},
{
    'number': 4, 'seats': 4
},
{
    'number': 5, 'seats': 8
}
]

# reservations = {}

def viewTables(tables):
    for table in tables:
        print(table)
# viewTables(tables)


reservations_file = 'reservations_file.csv'

def make_reservation(tables,reservations_file):
    name = input("Enter your name: ")
    contact = input("Enter your contact number: ")
    party_size = int(input("Enter the number of people: "))
    date = input("Enter reservation date (YYYY - MM - DD): ")
    start_time = input("Enter your starting time: ")
    end_time = input("Enter your ending time: ")

    
    available_table = [table for table in tables if table['seats'] >= party_size ]

    if not available_table:
        print("table not available for your party size")

    print("Available tables: ")
    for table in available_table:
        print(f"Table {table['number']} - seats: {table['seats']}")

 #table to reserve from available list
    table_number = int(input('Enter table number to reserve: '))

    if table_number not in [table['number'] for table in available_table]:
        print("invalid table number")
        return
    header= ["table_number", "name", "party_size", "contact", "date", "start_time", "end_time"]

    new_row= [table_number, name, party_size, contact, date, start_time, end_time]

    
    try:
        with open(reservations_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            if header:
                writer.writerow(header)
            writer.writerow(new_row)
        print(f"Table {table_number} reserved successfully for {name}")


    except Exception as e:
        print(f"error saving reservation: {e}")


# make_reservation(tables,reservations_file)

#Function to view reservations
def view_reservations(reservations_file):

        try:
            with open(reservations_file, "r") as file:
             reader = csv.reader(file)
            reservations = list(reader)
            for reservation in reservations:
                print(reservation)      
        except Exception as e:
         print("Error found")
        pass           
    
# view_reservations(reservations_file)


#Function to cancel reservations
def cancel_reservation(reservations_file):
    name = input("Enter your name: ")
    date = input("Enter the date of reservation: ")
    table_number = int(input("Enter table number: "))

    with open(reservations_file, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        reserves = list(reader)
        print(header)
        for reserve in reserves:
            if reserve[header.index('name')] == name and reserve[header.index('date')] == date and reserve[header.index('Table_number')] == table_number:
                reserve.remove
                print("Reservation for {name} cancelled successfully")
            else:
                print('reservation not found')
# cancel_reservation(reservation_file)


#Function to daily_summary reservations
def daily_summary(reservations_file):
    date = input("Enter date of reservation: ")
    try:
        with open(reservations_file, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            reservations = list(reader)
            correct_reservations = [r for r in reservations if r[header.index("date")] == date]
            if correct_reservations:
                for i in correct_reservations:
                    print(i)
                else:
                    print("No reservation found")
    except Exception as e:
        print('Invalid date')
        pass
# daily_summary(reservations_file)


#Function to modify reservations

def modify_reservation(reservations_file):
    date = input("Enter the date of the reservation to modify (YYYY - MM - DD): ")
    name = input("Enter the name of the reservation to modify: ")
    table_number = input("Enter the table number of the reservation to modify: ")

    try:
        # Read all reservations
        with open(reservations_file, "r", newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            reservations = list(reader)
        
        # Find and modify the reservation
        for b in reservations:
            if b[header.index("date")] == date and b[header.index("name")] == name and b[header.index("table_number")] == table_number:
                print("Current reservation details:", b)
                
                # Update the fields
                new_name = input(f"Enter new name (leave blank to keep current value '{b[header.index('name')]}'): ")
                if new_name:
                    b[header.index('name')] = new_name

                new_table_number = input(f"Enter new table number (leave blank to keep current value '{b[header.index('table_number')]}'): ")
                if new_table_number:
                    b[header.index('table_number')] = new_table_number

                new_date = input(f"Enter new date (leave blank to keep current value '{b[header.index('date')]}'): ")
                if new_date:
                    b[header.index('date')] = new_date
                
                # Write the updated reservations back to the CSV file
                with open(reservations_file, "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(reservations)

                print("Reservation updated successfully.")
                return  # Exit function after updating

        # If no reservation was found
        print("No reservation found for the given details.")
    
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# modify_reservation(reservations_file)

def reservationsystem():
    
    while True:
        print("1. Make a reservation")
        print("2. View reservations")
        print("3. Daily summary")
        print("4. Modify reservation")
        print("5. Quit")
        option = input("Choose an option: ")

        if option == "1":
            make_reservation(tables, reservations_file)
        elif option == "2":
            view_reservations(reservations_file)
        elif option == "3":
            daily_summary(reservations_file)
        elif option == "4":
            modify_reservation(reservations_file)
        elif option == "5":
            break
        else:
            print("Invalid option. Please try again.")


reservationsystem()