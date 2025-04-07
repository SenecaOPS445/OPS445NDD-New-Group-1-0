#!/usr/bin/env python3

import os
import sys
import argparse

# Function to list running processes
def list_processes():


# Function to search for a process by name
def search_process(name):

# Ali: Function to terminate a process by PID
def terminate_process(pid): # defines a function which takes the proccess ID as in put
    print(f"Terminating process with PID: {pid}") # print the following message to the user
    os.system(f'kill {pid}') # after running the "kill" command, it stops the process with that PID

if __name__ == "__main__":
