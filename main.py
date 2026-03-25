import sqlite3
from datetime import datetime

# STEP 3: Database Logic
def init_db():
    """Initializes the database and creates the notes table if it doesn't exist."""
    with sqlite3.connect('notes.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        ''')
        conn.commit()

# STEP 2: Logic for "Add a note"
def add_note():
    print("\n--- Add a New Note ---")
    title = input("Enter Title: ")
    content = input("Enter Content: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with sqlite3.connect('notes.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (title, content, created_at) VALUES (?, ?, ?)", 
                       (title, content, created_at))
        conn.commit()
    print(" Note saved successfully!")

# STEP 2: Logic for "View all notes"
def view_notes():
    print("\n--- All Saved Notes ---")
    with sqlite3.connect('notes.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes")
        rows = cursor.fetchall()
        
        if not rows:
            print("No notes found. Try adding one first!")
            return

        for row in rows:
            print(f"ID: {row[0]} | Title: {row[1]}")
            print(f"Date: {row[3]}")
            print(f"Content: {row[2]}")
            print("-" * 30)

# STEP 2: Logic for "Search notes"
def search_notes():
    print("\n--- Search Notes ---")
    query = input("Enter a keyword to search in titles: ")
    with sqlite3.connect('notes.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes WHERE title LIKE ?", (f'%{query}%',))
        rows = cursor.fetchall()
        
        if not rows:
            print(f"No notes found matching '{query}'.")
        else:
            for row in rows:
                print(f"ID: {row[0]} | Title: {row[1]} | Content: {row[2]}")

# STEP 2: Logic for "Delete a note"
def delete_note():
    print("\n--- Delete a Note ---")
    note_id = input("Enter the ID of the note you want to delete: ")
    with sqlite3.connect('notes.db') as conn:
        cursor = conn.cursor()
        # First check if it exists
        cursor.execute("SELECT title FROM notes WHERE id = ?", (note_id,))
        note = cursor.fetchone()
        
        if note:
            cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
            conn.commit()
            print(f" Note '{note[0]}' deleted successfully.")
        else:
            print(" Error: No note found with that ID.")

# STEP 4: Program Menu Example
def main():
    init_db()  # Ensure database is ready before the menu starts
    while True:
        print("\n============================")
        print("  Notes Management System")
        print("============================")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            search_notes()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print("Exiting program. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()