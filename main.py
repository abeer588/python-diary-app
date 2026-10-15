from diary import add_entry, load_diary, print_entries


def main():
    file_name = input("Enter diary filename, such as diary.txt: ")
    load_diary(file_name)

    while True:
        print("\n1. Add entry")
        print("2. Print entries by date")
        print("3. Load another diary file")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            entry_date = input("Enter date (YYYY-MM-DD): ")
            entry_text = input("Write your entry: ")
            add_entry(file_name, entry_date, entry_text)
            print("Entry saved.")

        elif choice == "2":
            entry_date = input("Enter date (YYYY-MM-DD): ")
            print_entries(file_name, entry_date)

        elif choice == "3":
            file_name = input("Enter another diary filename: ")
            load_diary(file_name)
            print("Diary file loaded.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()