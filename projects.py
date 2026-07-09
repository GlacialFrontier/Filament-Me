from storage import save_projects, load_projects
from utils import get_input, clear_screen, get_int, get_float



# store list of prints made
project_list = load_projects()

# view list of completed projects
def view_projects():
    print("\n--- Current Projects ---")

    if not project_list:
        print("No projects have been added.")
        return

    for i, project in enumerate(project_list, start=1):
        print(f"{i}. {project['name']} ({project['status']})")

    proj_sel = get_int(
        "\n Please select a Project Number to view the details ",
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

