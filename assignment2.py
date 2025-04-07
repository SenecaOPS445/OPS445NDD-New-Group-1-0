#!/usr/bin/env python3

import os
import argparse

# Function to list running processes, with optional filters
def list_processes(user=None, pid=None, state=None, text_filter=None):
    # Base ps command: show PID, USER, STATE, and full CMD
    cmd_parts = ['ps', '-eo', 'pid,user,state,cmd']

    # Build awk expressions for user, pid, state
    awks = []
    if user:
        awks.append(f'$2 == "{user}"')
    if pid:
        awks.append(f'$1 == {pid}')
    if state:
        # Match any of the state characters you supply (e.g. R, S, D, T, Z)
        awks.append(f'$3 ~ /[{state}]/')

    # If we have any awk filters, add them
    if awks:
        expr = ' && '.join(awks)
        cmd_parts += ['|', 'awk', f"'{expr}'"]

    # Finally, if you still want a free‑form grep
    if text_filter:
        cmd_parts += ['|', 'grep', f'"{text_filter}"', '|', 'grep -v grep']

    full_cmd = ' '.join(cmd_parts)
    print(f"Running: {full_cmd}")
    os.system(full_cmd)


# Function to search for a process by name
def search_process(name):
    print(f"Searching for process with name: {name}")
    os.system(f"ps aux | grep {name} | grep -v grep")

# Function to terminate a process by PID
def terminate_process(pid):
    print(f"Terminating process with PID: {pid}")
    os.system(f"kill {pid}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Manager Script")

    # Existing actions
    parser.add_argument('-l', '--list',    action='store_true', help="List processes")
    parser.add_argument('-s', '--search',  type=str,           help="Search by process name")
    parser.add_argument('-t', '--terminate',type=int,           help="Terminate by PID")

    # Filters for the list command
    parser.add_argument('-u', '--user',    type=str,           help="Only show this user’s processes")
    parser.add_argument('--pid',           type=int,           help="Only show this PID")
    parser.add_argument('--state',         type=str,           help="Only show processes in this state (e.g. R,S,D,T,Z)")
    parser.add_argument('-f', '--filter',  type=str,           help="Grep for this text after filtering")

    args = parser.parse_args()

    if args.list:
        list_processes(
            user=args.user,
            pid=args.pid,
            state=args.state,
            text_filter=args.filter
        )
    elif args.search:
        search_process(args.search)
    elif args.terminate:
        terminate_process(args.terminate)
    else:
        parser.print_help()
