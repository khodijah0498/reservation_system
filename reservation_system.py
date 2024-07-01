import csv
import os



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

# def make_reservation(tables, reservations):
def make_reservation(tables, reservations_file):
    name = input("Enter your name: ")
    contact = input("Enter your contact number: ")
    party_size = int(input("Enter the number of people: "))
    date = input("Enter reservation date (YYYY - MM - DD): ")
    start_time = input("Enter your starting time: ")
    end_time = input("Enter your ending time: ")

    # available_table = [table for table in tables if table['seats'] >= party_size and table['number'] not in reservations] 
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
    
    new_row= [table_number, name, party_size, contact, date, start_time, end_time]
    reservations_file = 'reservations_file.csv'
    # file_exist =os.path.isfile(reservations_file)

    try:
        with open(reservations_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            # writer.writerowAa("Table Number", "Name", "Party size")
            writer.writerow(new_row)
        print(f"Table {table_number} reserved successfully for {name}")


        # reservation = {'name': name, 'party_size': party_size}
        print(f"Table {table_number} reserved successfully for {name}.")
    except Exception as e:
        print(f"error saving reservation: {e}")


make_reservation(tables, reservations_file='reservation.csv')

def cancel_reservation(reservations_file, table_number):
    if table_number in reservations_file:
        del reservations_file[table_number]
        print(f"Reservation for table {table_number} cancelled successfully!")
    else:
        print(f"No reservation found for table {table_number}.")

    try:
        os.remove(reservations_file)
        print("File " + reservations_file + " deleted successfully. ")
    except IOError:
        print("Error: could not delete file " + reservations_file)

# cancel_reservation(table_number, reservations_file='reservation.csv')


def view_reservations(reservations_file):
    if not reservations_file:
        print("No reservations found.")
    else:
        for table_number, reservation in reservations_file.items():
            print(f"Table {table_number}: {reservation['name']} ({reservation['contact']}) - {reservation['party_size']} people, {reservation['date']} {reservation['start_time']} - {reservation['end_time']}")

    try:
        with open(reservations_file, 'r') as f:
            contents = csv.read(f)
            print(contents)

    except IOError:
        print("Error: could not read file " + reservations_file)
            

      
            
    

def main():
    while True:
        print("1. Make a reservation")
        print("2. Cancel a reservation")
        print("3. View reservations")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            make_reservation(tables, reservations_file= 'reservations.csv')
        elif choice == "2":
            table_number = int(input("Enter the table number to cancel: "))
            cancel_reservation(reservations_file='', table_number)
        elif choice == "3":
            view_reservations(reservations_file= 'reservations.csv')
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")