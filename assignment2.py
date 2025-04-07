#!/usr/bin/env python3

import os
import sys
import argparse

# Function to list running processes
def list_processes():

# Samip: Function to search for a process by name
def search_process(name):       
    print(f"Searching for process with name : {name}") # prints the search message to the user
    os.system(f'ps aux | grep {name}') # It filters the search result

# Function to terminate a process by PID
def terminate_process(pid):

if __name__ == "__main__":
    


    parser.add_argument('-s', '--search', type=str, help="Search for a process by name")

    if 

    elif args.search: #Samip: If -s or --search is passed
        search_process(args.search) #Samip: It calls the funtion to search

    elif 

    else: