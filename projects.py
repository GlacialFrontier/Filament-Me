from storage import save_projects, load_projects
from utils import get_input, clear_screen, get_int, get_float



# store list of prints made
project_list = load_projects()

PROJECT_FIELDS = {
                1: ("name", "Project Name"),
                2: ("orig_file_type", "File Type"),
                3: ("filament_type", "Filament Type"),
                4: ("filament_color", "Filament Color"),
                5: ("filament_used", "Filament Used"),
                6: ("print_time", "Print Time"),
                7: ("status", "Status"),
                8: ("notes", "Notes")
            }

# view list of completed projects
def view_projects():
    print("\n--- Current Projects ---")

    if not project_list:
        print("No projects have been added.")
        return

    for i, project in enumerate(project_list, start=1):
        print(f"{i}. {project['name']} ({project['status']})")

    proj_sel = get_int(
        "\nPlease select a Project Number to view the details ",
        minimum=0, 
        maximum=len(project_list)
    )
    
    if proj_sel is None or proj_sel == 0:
        return
    
    project = project_list[proj_sel - 1]
    view_project_details(project)

# method to see the details of the selected project
def view_project_details(project):

    clear_screen()

    print("\n==========================")
    print("     Project Details")
    print("==========================")

    print(f"Name: {project['name']}")
    print(f"File Type: {project['orig_file_type']}")

    print("\n--- Filament ---")
    print(f"Type: {project['filament_type']}")
    print(f"Color: {project['filament_color']}")
    print(f"Weight: {project['filament_used']} g")

    print("\n--- Print ---")
    print(f"Time: {project['print_time']}")
    print(f"Status: {project['status']}")

    print("\n--- Notes ---")
    print(project['notes'])

    input("\nPress Enter to return...")


# method to add a new print to the project_list
def add_project():
    print("\n --- Add a New Project ---")

    # prompt for Proj Name
    name = get_input("Project Name: ")
    if name is None:
        return
    
    # prompt for Proj File Typ
    orig_file_type = get_input("File Type: \n(e.g. 3mf, step, obj, etc.) ")
    if orig_file_type is None:
        return
    
    # prompt for Proj Fila Typ
    filament_type = get_input("Filament Type \n(e.g. PLA, TPU, PETG, etc.)")
    if filament_type is None:
        return
    
    # prompt for Proj Fila Color
    filament_color = get_input("Filament Color: ")
    if filament_color is None:
        return

    # prompt for Proj est Fila Weight
    grams = get_float("Estimated Grams Used: ")
    if grams is None:
        return
    
    # prompt for Proj Prnt Time
    print_time = get_input("Print Time (hh:mm): ")
    if print_time is None:
        return
    
    # prompt for Proj Stat
    status = get_input("Print Status: ")
    if status is None:
        return
    
    # prompt for Proj Notes
    notes = get_input("General Notes: ")
    if notes is None:
        return

    # Local save to Project
    save_project(name,orig_file_type,filament_type,filament_color,grams,print_time, status, notes)



# save project to the Project dictionary [locally]
def save_project(name: str, orig_file_type:str, fila_typ: str, fila_color: str, fila_used: float, prnt_time: float, status: str, notes: str):

    # dictionary for project
    project = {
        "name": name,
        "orig_file_type": orig_file_type,
        "filament_type": fila_typ, # pla/pet/tpu
        "filament_color": fila_color, 
        "filament_used": fila_used, # in grams
        "print_time": prnt_time, # minutes
        "status": status,
        "notes": notes
    }

    # add the project to the list
    project_list.append(project)

    # move project to JSON file
    save_projects(project_list)


    print(f'\n \n--- Project Successfully Added ---\n')
    
    view_project_details(project)

# edit projects
def edit_project():
        print("\n--- Edit/Delete Projects ---\n")
        print("Choose a project to Modify/Delete\n")

        if not project_list:
            print("No projects exist to edit.")
            return

        for i, project in enumerate(project_list, start=1):
            print(f"{i}. {project['name']} ({project['status']})")

        proj_sel = get_int(
            "\nPlease select a Project Number you wish to edit: ",
            minimum=0, 
            maximum=len(project_list)
        )
    
        if proj_sel is None or proj_sel == 0:
            return
    
        project = project_list[proj_sel - 1]
        view_project_details(project)

        print(f"What would you like to do with {project['name']}?")
        print("\n1. Edit Project")
        print("\n2. Delete Project")
        option_sel = get_int(
            "\n\nSelect an option to contine. Select 3 to return to Project selection. " \
            ""
        )
    
        if option_sel is None or option_sel == 3:
            return
        
        if option_sel == 1:

            for menu_num, (field, label) in PROJECT_FIELDS.items():
                print(f"{menu_num}. {label}")
                
            # get the number from the prompt
            sel_proj_field = get_int(
                "\nPlease select a Project Number you wish to edit: ",
                minimum=1, 
                maximum=len(PROJECT_FIELDS)
            )

            if sel_proj_field == None:
                return
            
            # get current record.
            editing_field = PROJECT_FIELDS[sel_proj_field][0]
            curr_data = project[editing_field]
            print("--- Field ----")
            print(f"{editing_field}: {curr_data}")

            # request new value.
            if editing_field == "filament_used":
                new_data = get_float("Please provide your update: ")
            else:
                new_data = get_input("Please provide your update: ")
            
            # update old value with new value.
            if curr_data == new_data:
                print("Data Unchanged")
                return
            
            project[editing_field] = new_data

            save_projects(project_list)

            print("--- Project Updated Successfully ---")
            print(f"Field Changed: {editing_field}")
            print(f"\nPrevious Data: {curr_data}")
            print(f"Updated Data: {new_data}")

            # save records [not sure if needed]

        if option_sel == 2:
            print(f"Do you wish to delete: {project['name']}\n")
            print("\n 1. Yes \n 2. No")
            #delete method goes here