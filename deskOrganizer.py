import os
import sys
import shutil

FILE_EXTENSIONS = {
    ".png" : "Photos",
    ".jpeg" : "Photos",
    ".jpg" : "Photos",
    ".gif" : "Photos",
    ".doc" : "Documents",
    ".word" : "Documents",
    ".txt" : "Documents",
    ".pdf" : "PDFs",
    ".mp4" : "Videos",
    ".mp3" : "Music",
    ".wav" : "Music"
}

FOLDERS = ["Photos", "Documents", "PDFs", "Videos", "Music"]

def create_dir(path):
    # If folder already exists, print exception, move on
    try:
        os.mkdir(path)
    except:
        print("Folder already created")

def gather_files(source):
    all_files = []

    og_cwd = os.getcwd()
    os.chdir(source)
    cwd = os.getcwd()
    dir_length = len(cwd)
    cwd_end = ""
    counter = 0
        
    # Gathers all files from folder (source) 
    for root, dirs, files in os.walk(source):
        for f in files:
            # Makes sure to only sort files in source and not in any deeper folders
            weed_out = source + "\\" + f
            if os.path.exists(weed_out):
                all_files.append(f)

    return all_files

def main(target):
    # Create folders for sorting
    length = len(FOLDERS)
    for i in range(length):
        new_dir = target + "\\" + FOLDERS[i]
        create_dir(new_dir)
    
    files = gather_files(target)

    for i in files:
        # Find the file extension
        file_length = len(i)
        dot_what = file_length-4
        file_end = i[dot_what:]
        
        # Move file to corresponding folder
        for j in FILE_EXTENSIONS:
            if j == file_end:
                old_dir = target + "\\" + i 
                new_dir = target + "\\" + FILE_EXTENSIONS[j] + "\\" + i
                shutil.move(old_dir, new_dir)

# Grabs folder to be sorted from command line
if __name__ == "__main__":
    args = sys.argv
    
    # Process to get full directory even if there are spaces
    length = len(args)
    target = ""
    for i in range(length-1):
        if i == 0:
            target = args[1]
        else:
            target = target + " " + args[i+1]

    main(target)