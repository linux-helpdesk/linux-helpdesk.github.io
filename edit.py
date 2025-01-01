import os
import sys
import time

struct_yes = time.localtime((time.time() - 24 * 60 * 60))
date = f"{str(struct_yes.tm_year)}-{str(struct_yes.tm_mon)}-{struct_yes.tm_mday}-"

# Read file name and check ral-full path or not
raw_file = sys.argv[1]
if "_posts/" in raw_file:
    file = raw_file
else:
    file = os.path.join("_posts", date + raw_file)

file_list = os.listdir("_posts")

# Check exists and copy template file
if file.split("/")[-1] not in file_list:
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
