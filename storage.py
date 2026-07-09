import json
import os

# script to save Project data as needed for program
def save_projects(project_list):
    with open("data/projects.json", "w") as file:
        json.dump(project_list, file, indent=4)

# script to load Project data as needed for View & edit
def load_projects():

    # file location
    filename = "data/projects.json"

    # identify if file not found
    if not os.path.exists(filename):
        print("No file found. Please add a new project.")
        return []
    
    # identify if file contains any data (if file size is 0bytes)
    if os.path.getsize(filename) == 0:
        print("No records found. Please add a new project.")
        return []
    
    # raise exception if json file gets corrupt
    try:
        # if file contains data, load it for the system to utilize.
        with open(filename, "r") as file:
            projects = json.load(file)

        print (f"Loaded {len(projects)} project(s).")

        return projects
    
    except json.JSONDecodeError:
        print("WARNING: the projects.json file is corrupted.")
        return []