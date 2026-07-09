from storage import save_projects, load_projects


# store list of prints made
project_list = load_projects()

# view list of completed projects
def view_projects():
    print("\n--- Current Projects ---")

    if not project_list:
        print("No projects have been added.")
        return

    for i, project in enumerate(project_list, start=1):
        print(f"{i}. {project['name']}")

# method to add a new print to the project_list
def add_project():
    print("\n --- Add a New Project ---")

    name = input("Project Name: ")
    orig_file_type = input("File Type: \n(e.g. 3mf, step, obj, etc.) ")
    filament_type = input("Filament Type \n(e.g. PLA, TPU, PETG, etc.)")
    filament_color = input("Filament Color: ")
    grams = float(input("Estimated Grams Used: "))
    print_time = input("Print Time (hh:mm): ")
    status = input("Print Status: ")
    notes = input("General Notes: ")

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
    print(f'--- Project Details: --- ')
    print(f'Project Name: {project["name"]}')
    print(f'Project Original File Type: {project["orig_file_type"]}')
    print(f'\n--- Filament Info ---')
    print(f'Type: {project["filament_type"]}')
    print(f'Color: {project["filament_color"]}')
    print(f'Weight: {project["filament_used"]}')
    print(f'\n--- Print Info ---')
    print(f'Time Taken: {project["print_time"]}')
    print(f'Current Staus: {project["status"]}')
    print(f'\n--- General Notes ---')
    print(f'Notes: {project["notes"]}')

