# Function to add data to the file
def add_data():
    with open("data.txt", "a") as file:
        data = input("Enter data to store: ")
        file.write(data + "\n")
    print("Data added successfully!")

# Function to view all stored data
def view_data():
    try:
        with open("data.txt", "r") as file:
            data = file.readlines()
            if data:
                print("Stored Data:")
                for line in data:
                    print(line.strip())
            else:
                print("No data stored yet.")
    except FileNotFoundError:
        print("No data stored yet.")

# Function to clear all stored data
def clear_data():
    try:
        open("data.txt", "w").close()
        print("All data cleared successfully!")
    except FileNotFoundError:
        print("No data stored yet.")

# Main function to run the program
def main():
    while True:
        print("\nMenu:")
        print("1. Add Data")
        print("2. View Data")
        print("3. Clear Data")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_data()
        elif choice == "2":
            view_data()
        elif choice == "3":
            clear_data()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
