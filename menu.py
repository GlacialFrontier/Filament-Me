
import os
from projects import view_projects

main_menu_options = [
    "Projects",
    "Filaments",
    "Stats",
    "back"
]

proj_sub_menu_options = [
    "View all Projects",
    "Add a new Project",
    "Edit/Delete an existing Project",
    "back"
]

fila_sub_menu_options = [
    "View all Filaments",
    "Add a new Filament",
    "Edit/Delete an existing Filament",
    "back"
]

stats_sub_menu_options = [
    "View Stats",
    "back"
]

# clear screen method
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# create main Nav()
def main_menu():
    while True:
        clear_screen()

        print("\n==== Main Menu ====")
        for i, option in enumerate(main_menu_options, start=1):
            print(f"{i}. {option}")

        choice = input("Please select an option: ")

        if choice == "1":
            project_menu()
        elif choice == "2":
            filament_menu()
        elif choice == "3":
            stats_menu()
        elif choice == "4":
            break
        else:
            print("Invalid Choice. Please Try again.")

def project_menu():
    while True:
        clear_screen()
        
        print("\n==== Projects ====")
        for i, option in enumerate(proj_sub_menu_options, start=1):
            print(f"{i}. {option}")

        choice = input("Please select an option: ")

        if choice == "1":
            view_projects()

        elif choice == "2":
            add_project()

        elif choice == "3":
            edit_project()

        elif choice == "4":
            return

        else:
            print("Invalid selection.")

def add_project():
    print("--- Adding New Project ---")

def edit_project():
    print("--- Modify an existing Project")


def filament_menu():
    while True:
        clear_screen()
        
        print("\n==== Filaments ====")
        for i, option in enumerate(fila_sub_menu_options, start=1):
            print(f"{i}. {option}")

        choice = input("Please select an option: ")

        if choice == "1":
            view_filaments()

        elif choice == "2":
            add_filament()

        elif choice == "3":
            edit_filament()

        elif choice == "4":
            return

        else:
            print("Invalid selection.")  

def view_filaments():
    print("--- View current filaments ---")

def add_filament():
    print("--- Adding New Filament ---")

def edit_filament():
    print("--- Modify an existing Filament ---")


def stats_menu():
    while True:
        clear_screen()
        
        print("\n==== Statistics ====")
        for i, option in enumerate(stats_sub_menu_options, start=1):
            print(f"{i}. {option}")

        choice = input("Please select an option: ")

        if choice == "1":
            view_stats()

        elif choice == "2":
            return

        else:
            print("Invalid selection.")     
     
def view_stats():
    
    print("--- Viewing Stats ---")