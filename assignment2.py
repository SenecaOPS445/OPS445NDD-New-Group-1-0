#!/usr/bin/env python3

import os
import sys
import argparse

# Function to list running processes
def list_processes():

# Function to search for a process by name
def search_process(name):
    print(f"Searching for process with name : {name}")
    os.system(f'ps aux | grep {name}')

# Function to terminate a process by PID
def terminate_process(pid):

if __name__ == "__main__":