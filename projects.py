# store list of prints made
project_list = ()

# view list of completed projects
def view_projects():
    print("Here are the list of your current projects. \n Select one to review:")
    print(project_list)

# method to add a new print to the project_list
#def add_project():
#    while True:


# save project to the Project dictionary
def save_project(name: str, orig_file_type:str, fila_typ: str, fila_color: str, fila_used: float, prnt_time: float):

    # dictionary for project
    project = {
        "name": name,
        "orig_file_type": orig_file_type,
        "filament_type": fila_typ, # pla/pet/tpu
        "filament_color": fila_color, 
        "filament_used": fila_used, # in grams
        "print_time": prnt_time, # minutes
    }

    # add the project to the list
    project_list.append(project)


    print(f'--- Project Successfully Added ---')
    print(f'--- Project Details: --- ')
    print(f'Project Name: {name}')
    print(f'Project Original File Type: {orig_file_type}')
    print(f'--- Filament Info ---')
    print(f'Type: {fila_typ}')
    print(f'Color: {fila_color}')
    print(f'Weight: {fila_used}')
    print(f'--- Print Info ---')
    print(f'Time Taken: {prnt_time * 60} hours')

