def load_diary(file_name):
    with open(file_name, "a", encoding="utf-8"):
        pass


def add_entry(file_name, entry_date, entry_text):
    with open(file_name, "a", encoding="utf-8") as diary_file:
        diary_file.write(entry_date + " | " + entry_text + "\n")


def print_entries(file_name, entry_date):
    found = False

    with open(file_name, "r", encoding="utf-8") as diary_file:
        for line in diary_file:
            if line.startswith(entry_date + " | "):
                print(line.strip())
                found = True

    if not found:
        print("No entries found for this date.")