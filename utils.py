import os

# Input check for cancellations on requests
def get_input(prompt):
    # variable to get initial prompt + the cancellation check
    value = input(f"{prompt} (or type 'cancel'): ")

    # if user types 'cancel' then return the user to the previous menu
    if value.lower() == "cancel":
        return None
    
    return value

# Function to clear CLI Screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# initiate prompt to pause CLI before moving on
def pause():
    input("\n Press Enter to continue...")

# initiate prompt to pause CLI before returning
def return_prompt():
    input("\n Press Enter to return...")

# variable to get initial prompt + the cancellation check (for view deets)
def detail_return(prompt):
    value = input(f"\n {prompt} (or select '0' to return): ")

    # if user types 'cancel' then return the user to the previous menu
    if value.lower() == "0":
        return None
    
    return value

def get_int(prompt, minimum=None, maximum=None):
    while True:
        value = input(prompt)

        if value.lower() == "cancel":
            return None
        
        if not value.isdigit():
            print("Please enter a valid number.")
            continue

        value = int(value)
        
        if minimum is not None and value < minimum:
            print(f"Please enter a number greater than or equal to {minimum}.")
            continue

        if maximum is not None and value > maximum:
            print(f"Please enter a number less than or equal to {maximum}.")
            continue

        return value
        
def get_float(prompt):
    value = get_input(f"{prompt}, or type cancel.")

    if value is None:
        return
    
    value = float(value)

    return value