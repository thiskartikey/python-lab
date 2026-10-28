import os
import sys

# Show current directory path
print("Current Directory:", os.getcwd())

# List items in directory
print("\nContents of Current Directory:")
for entry in os.listdir():
    print(entry)

# Create a project workspace directory
target_dir = "workspace"

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print("\nWorkspace folder created.")
else:
    print("\nWorkspace folder already exists.")

# Move into the workspace
os.chdir(target_dir)
print("Current Directory:", os.getcwd())

# Append to activity log
log_name = "system_log.txt"
with open(log_name, "a") as log_file:
    log_file.write("System utility executed successfully.\n")

print("\nLog file created/updated:", log_name)

# List text documents in current directory
print("\nText Files:")
for file_item in os.listdir():
    if file_item.endswith(".txt"):
        print(file_item)

# Read log file contents safely
print("\nLog File Content:")
with open(log_name, "r") as log_file:
    log_content = log_file.read()
    print(log_content)

# Return to parent directory
os.chdir("..")
print("Returned to:", os.getcwd())

# Show command-line arguments
print("\nCommand-line Arguments:")
for cli_arg in sys.argv:
    print(cli_arg)
