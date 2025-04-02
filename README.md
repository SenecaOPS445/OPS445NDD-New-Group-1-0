# Winter 2025 Assignment 2

# 🧩 Process Manager Script

A Python script to list, search, and terminate running processes on a Linux system using command-line arguments.

## 📥 How Input is Gathered

Input is collected through *command-line arguments*, parsed using Python’s argparse module.

Supported arguments:
- --list – List all currently running processes.
- --search <process_name> – Search for processes by name.
- --kill <pid> – Terminate a process by its process ID.

## ⚙️ How the Program Works

The script utilizes the subprocess module to interact with the system:

- Runs ps, grep, and kill commands via Python to interact with processes.
- Filters and parses process information from command output.
- Gracefully handles user errors and invalid input.
- Confirmation is requested before process termination.

## 📤 Output Format

- --list and --search: Display process information (PID, name, user, etc.) directly in the terminal.
- --kill: Prompts for confirmation, then returns success or error messages depending on whether the termination was successful.

## 🛠️ Command-Line Options

| Argument         | Description                                      |
|------------------|--------------------------------------------------|
| --list         | Lists all running processes                      |
| --search       | Filters and displays matching processes by name |
| --kill <pid>   | Terminates the specified process ID             |

## 🧱 Challenges Expected

- Handling permission issues when attempting to kill system processes
- Parsing process information reliably across different Linux distributions
- Preventing unintentional termination of important system processes
- Providing clear and safe prompts and messages to users
- Ensuring robustness and graceful failure for invalid input

## 🗓️ Project Timeline

### Week 1: March 18 - March 24 (Planning & Setup)
- 🗓️ *March 18-19*:
  - Project scope finalized
  - GitHub repository created and branches set up
- 🛠️ *March 20-24*:
  - --list implementation and testing by Member 1
  - --search <process_name> implementation by Member 2
  - --kill planning and documentation structure outlined by Member 3
  - Initial test cases created

### Week 2: March 25 - March 31 (Development & Testing)
- 💻 *March 25-26*:
  - Finalizing --list and debugging
  - Adding partial match support in --search
  - Starting implementation of --kill with error checks
- 🧪 *March 27-28*:
  - Internal testing of --list and --search
  - Add confirmation prompt in --kill
  - Team-wide code review and error handling improvements
- ✅ *March 29-31*:
  - Debugging and cross-checking all functions
  - Writing unit tests
  - Begin drafting this README.md

### Week 3: April 1 - April 6 (Finalization)
- 🧹 *April 1-2*:
  - Finalize error handling
  - Test across multiple Linux environments (Matrix, MyVMLab)
  - Add git logs for contribution tracking
- 📝 *April 3-4*:
  - Finalize README.md
  - Ensure all features are functional and clean
- 🔚 *April 5-6*:
  - Merge branches to main, tag release v1.0
  - Prepare and practice live demo

### Final Day: April 7
- 🧪 Live demo and walkthrough
- 📄 Git log and commit verification
- ✍️ Individual post-mortem reports submitted

---

## 💻 Example Usage

```bash
# List all running processes
python3 process_manager.py --list

# Search for a process named "chrome"
python3 process_manager.py --search chrome

# Kill a process with PID 12345
python3 process_manager.py --kill 12345