from datetime import datetime

class JournalManager:
    def __init__(self):
        self.entries=[]

    def create_entry(self, entry):
        timestamp=datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        self.entries.append(f"{timestamp}\n{entry}")
        print("Entry added successfully!\n")

    def view_entries(self):
        if not self.entries:
            print("No journal entries found. Start by adding a new entry!.\n")
        else:
            print("\nOutput:")
            for entry in self.entries:
                print("-" * 20)
                print(entry)
            print()

    def search_entry(self, keyword):
        found_entries=[entry for entry in self.entries if keyword.lower() in entry.lower()]
        if not found_entries:
            print(f"No entries found with that keyword: {keyword}\n")
        else:
            print("\nOutput:")
            for entry in found_entries:
                print("-" * 20)
                print(entry)
            print()

    def delete_all_entries(self):
        confirm=input("Are you sure you want to delete all entries? (yes/no): ").strip().lower()
        
        if confirm=="yes":
            self.entries.clear()
            print("All entries deleted successfully!\n")
        elif confirm=="no":
            print("Deletion cancelled. Entries were kept.\n")
        else:
            print("Invalid input. Action cancelled.\n")
        

journal_manager=JournalManager()

print("Welcome to Personal Journal Manager")
while True:
    print("Choose an operation:")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search for an entry")
    print("4. Delete all entries")
    print("5. Exit")

    try:
        choice=int(input("User Input: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.\n")
        continue

    if choice==1:
        entry=input("Enter your journal entry: ")
        journal_manager.create_entry(entry)
    elif choice==2:          
        journal_manager.view_entries()
    elif choice==3:
        keyword=input("Enter a keyword to search: ")
        journal_manager.search_entry(keyword)
    elif choice==4:          
        journal_manager.delete_all_entries()
    elif choice==5:
        print("Exiting the Personal Journal Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")