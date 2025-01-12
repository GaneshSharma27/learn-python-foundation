# ------------------ Reading and writing files ------------------
# file has two properties namely 'filename' and 'path'
# path specifies the location of the file on the computer
# the last part of the filename after the last period is called file's extension and it tells the file's type

# --------------- Backslash on windows and forward slash on macOS and linux ---------------
# '\' are used as a separator between folder names in windows
# '/' are used as a separator between folder names in macOS and linux
# for making program to work on both operating systems, you'll have to write the python scripts to handle both cases
# this can be done by using 'Path()' function in 'pathlib' module
import os
from pathlib import Path
file_path = Path("Spam", "Bacon", "Eggs")
print("Path:", file_path)
print()

# --------------------- another program ---------------------
my_files_list = ["accounts.txt", "details.csv", "invite.docx"]
for filename in my_files_list:
    print(Path(r"C:\Users\Ganesh", filename))
print()

# ------------ Using the '/' operator to join paths ------------
path_1 = Path("spam") / "bacon" / "eggs"
path_2 = Path("spam") / Path("bacon/eggs")
path_3 = Path("spam") / Path("bacon", "eggs")
print("Path 1:", path_1)
print("Path 2:", path_2)
print("Path 3:", path_3)
print()

# ----------------- Current working directory -----------------
# every program that runs on your computer has a current working directories
# any filename or path that doesn't begin with the root directory, they're assumed to be under the current working directories
print("Current working directory:", Path.cwd())
# os.chdir("C:\\Users")         # for changing directory
# os.getcwd()                   # for older way of getting the current working directory
# there's no 'pathlib' function for changing the working directory, it can lead to bugs

# -------------------- Home directory --------------------
print("Home directory:", Path.home())
print()

# ----------------- Absolute vs Relative Paths -----------------
"""
    absolute path, which always begins with the root folder
    relative path, which always begins with the program's current working directory
    dots are used to give special names to the folders, although these aren't real name given to the folders
    single dot '.' for a folder name is shorthand for "This directory"
    double dot '..' for a folder name is shorthand for "The parent folder"
"""

# ---------------- Creating new folder using the 'os.makedirs()' function ----------------
# os.makedirs("D:\\Programming\\Python Fundamentals\\Test folder")        # this'll create a new folder
# even if ..\Programming folder wouldn't have existed then too the 'makedirs()' will create that '..\Programming\' folder 
# along with 'Python Fundamentals' and 'Test folder' in '..\Programming\' and '..\Programming\Python Fundamentals\' respectively

# ------------- Creating new folder using 'Path' object and 'pathlib()' function -------------
# Path(r"D:\\Programming\\Python Fundmentals\\Test folder\\Test folder (using Path object)").mkdir()
# 'makedir()' can only make one directory at a time, it won't be able to make sub-directories all at once like 'os.makedirs()'

# ------------------ Handling absolute and relative path ------------------
print("Path:", Path.cwd())
print("Path is absolute?:", Path.cwd().is_absolute())
print("Check whether 'spam/bacon/eggs' are absolute or not?:", Path("spam/bacon/eggs").is_absolute())
print()
print(Path("my/relative/path"))
print(Path.cwd() / Path("my/relative/path"))    # writing 'Path.cwd() /' gives the absolute path for the relative path
print(Path.home() / Path("my/relative/path"))   # if relative path is relative to another path beside the cwd, 
# then replace 'Path.cwd()' with that other path
print()

# ------------------ Handling absolute and relative path using 'os.path()' ------------------
"""
    os.path.abspath(path) ---> returns a string of absolute path, easy way of converting a relative path to absolute path
    os.path.isabspath(path) ---> returns 'True' if the arguments is an absolute path and 'False' if it is relative path
    os.path.relpath(path, start) ---> returns a string of relative path from 'start' path to 'path', if 'start' path is provided
                                      then the cwd is used as 'start' path
"""
print(os.path.abspath("."))
print(os.path.abspath(".\\Scripts"))
print(os.path.isabs("."))
print(os.path.isabs(os.path.abspath(".")))
# the single dot '.' represents the absolute path
print()
print(os.path.relpath("C:\\Windows", "C:\\"))
print(os.path.relpath("C:\\Windows", "C:\\spam\\eggs"))
print()
# when a relative path is within the same parent folder as the path, but within subfolders of different path, you can then use
# '..' notation to return to the parent folder

# ------------------ Getting the parts of a file path ------------------
"""
    The parts of the file path include
    1. The anchor, which is the root folder of the filesystem. The drive letter on windows.
    2. The parent, which is the folder that contains the file.
    3. The name of the file, made up of the stem (base name) and the suffix (extension).
"""
p = Path("D:/Coding/Python tutorial - Automate the boring stuff/00_Documentation.txt")
print("Anchor --->", p.anchor)
print("Parent --->", p.parent)
print("Name --->", p.name)
print("Stem --->", p.stem)
print("Suffix --->", p.suffix)
print("Drive --->", p.drive)
# all of them above evaluate to simple string values, except 'parent' which evaluates to another 'Path' object
print()

# ----------------- 'parents' attribute which evaluates to the ancestor folders of a Path object -----------------
print("Current working directory --->", Path.cwd())
print("Current working directory using parents --->", Path.cwd().parents[0])    # as indexing increases the 'parents'
#                                                                      keeps on getting to its parent folder or directory
print("Current working directory using parents --->", Path.cwd().parents[1])
# print("Current working directory using parents --->", Path.cwd().parents[2])  # will give 'indexError'
print()

# -------------- using os.path for getting the different parts of the path written in a string value --------------
calc_file_path = "C:\\Windows\\System32\\calc.exe"
print("Basename:", os.path.basename(calc_file_path))
print("Directory name:", os.path.dirname(calc_file_path))
# if you need both of them then use
print("Both:", os.path.split(calc_file_path))   # os.path.split() returns both basename and directory name in tuple
print()

# ------------------------ Finding file size and folder contents ------------------------
print("Size in bytes:", os.path.getsize("C:\\Windows\\System32\\calc.exe"))     # returns file size in bytes
print("Directories in D:\\Coding:", os.listdir("D:\\Coding"))          # returns a list of filename strings for each file
#           in the argument. Also this is not function of 'os.path' but of 'os'

# finding total size of 'C:\\Windows\System32'
total_size = 0
for each_file in os.listdir("C:\\Windows\\System32"):
    total_size = total_size + os.path.getsize(os.path.join("C:\\Windows\\System32", each_file))
print("Total size of System32 is", total_size)

# -------------------- Modifying a list of files using Glob patterns --------------------
p = Path("C:\\Users\\ganes\\OneDrive\\Desktop")
print(p.glob("*"))      # glob() method returns a generator object
# that will be needed to pass into the list() to easily view it
# the asterisk stands for multiple of any characters
print("List view:", list(p.glob("*")))

