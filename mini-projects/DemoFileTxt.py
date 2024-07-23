import os

# Define the path to the Documents directory and the file name
documents_dir = os.path.join(os.path.expanduser("~"), "Documents")
file_path = os.path.join(documents_dir, "demofile.txt")

# Ensure the Documents directory exists
if not os.path.exists(documents_dir):
    os.makedirs(documents_dir)

# Create and write to the file
with open(file_path, "w") as f:
    f.write("This is a sample content for demofile.txt.")

print(f"File created at: {file_path}")