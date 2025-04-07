#!/usr/bin/env python3

import os
import argparse

# Logan: Function to list running processes
def list_processes(user=None):
    if user: # Logan: If user value is provided continue
        cmd = f"ps -u {user}" # Logan: Creating variable to allow the processes to be filtered by user since it was provided
        print(f"\nListing all processes under user {user}.\n")
        os.system(cmd)
    else: # Logan: If no user provided
         cmd = "ps aux" # Logan: Creating variable to list all processes since no user value provided.
         print(f"\nListing all processes.\n")
         os.system(cmd)


# Samip: Function to search for a process by name
def search_process(name):       
    print(f"Searching for process with name : {name}") # prints the search message to the user
    os.system(f'ps aux | grep {name}') # It filters the search result
    
# Ali: Function to terminate a process by PID
def terminate_process(pid): # defines a function which takes the proccess ID as in put
    print(f"Terminating process with PID: {pid}") # print the following message to the user
    os.system(f'kill {pid}') # after running the "kill" command, it stops the process with that PID

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Manager Script") # Initialize argument parser with a description for -h
    parser.add_argument('-t', '--terminate', type=int, help="Terminate a process by PID") # Ali: adds a command line option with a help text
    parser.add_argument('-l', '--list', action='store_true', help='List processes') # Logan: adds a command line argument so the user can list processes
    parser.add_argument('-u', '--user', type= str, help='Filter processes by user') # Logan: adds a command line argument to use with the list argument to filter user processes
    parser.add_argument('-s', '--search', type=str, help="Search for a process by name") # Samip: adds a command line argument to search for the processes
    args = parser.parse_args() # Parse command line arguments and store them in args so we can call them when arguments are used.

    if args.list: # Logan: if user uses -l or --list then continue
        list_processes(args.user) # Logan: Calls the list process along with args.user which holds the value of the user provided, if none then args.user will not be used
        
    elif args.search: #Samip: If -s or --search is passed
        search_process(args.search) #Samip: It calls the funtion to search
        
    elif args.terminate: # Ali: if user uses -t or --terminate options
        terminate_process(args.terminate) # Ali: call the function to terminate the process using the PID
    else:
        print("Please provide a valid option. Use -h for help.") 
