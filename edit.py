import os
import sys

# Read file name
file = sys.argv[1]

file_list = os.listdir("_posts")

# Copy template file
os.system(f"cp template.md {file}")

# Open or creat file
os.system(f"nvim {file}")

os.system("git add .")

# Check and add comments
if file.split("/")[-1] in file_list:
    os.system(f"git commit -m 'Updated {file}'")
else:
    os.system(f"git commit -m 'Added {file}'")

# Push
os.system("proxychains4 git push")
