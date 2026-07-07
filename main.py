#import streamlit as st
from projects import view_projects
from menu import main_menu

def main():

    # CLI title page (note: to use Streamlit for GUI)
    #st.text("--- Weclome to Filament & Me ---")
    #st.text("\nThis tool is used to track projects, Filaments and that yummy stats on both.")

    print("--- Weclome to Filament & Me ---")
    print("\nThis tool is used to track projects, " \
            "Filaments and that yummy stats on both.\n\n " \
            "--- To begin please provide us with the following: --- \n")
    
    main_menu()
if __name__ == "__main__":
    main()