# Add the code for the file counter script that you wrote in the course.
# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
from pprint import pprint  #to pretty print (pprint) the dictionary
import pathlib
from pathlib import Path
from datetime import datetime  #to record the time the script was run

# The path where we want to create the new folder
folder_directory = pathlib.Path('/Users/francescapanteli/Desktop')
# this is an absolute path, which means the script can be run from anywhere

files_on_desktop = []
files_on_desktop_counter = 0
png_counter = 0

# loop through everything on the Desktop
for file in folder_directory.iterdir():
    if len(file.suffix) > 0:  # some of the file suffixes are '', with lengths of 0
        files_on_desktop.append(file.suffix)
    if file.suffix == '.png':
        png_counter += 1  # count the number of png files on the desktop
    else:
        files_on_desktop_counter += 1  # counts the number of folders (and other non-png items)

# create a dictionary of file types and their counts
keys = list(set(files_on_desktop))
values = [files_on_desktop.count(i) for i in keys]
dictionary = dict(zip(keys, values))

print("Desktop file summary: ", dictionary)

# get the current date and time the script was run
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #the time that the script is run, using the datetime module

# write the desktop data to a file
file_out = open("Desktop file summary.sql", "a")  # "w" would overwrite, so we use append
# this was changed to a csv file, rather than a txt file, during the third module exercises of the course
# change this to append because we are counting how the number of files on the desktop changes over time
# this was later changed to an sql file
file_out.write("\n")
file_out.write("Desktop file summary: " + str(dictionary) + "\n")
file_out.write(f"Script run at: {timestamp}\n") #using an f string literal to write the time that the script was run, to the sql file
file_out.write("Number of pngs on desktop: " + str(png_counter) + "\n")
file_out.write("Number of folders on the desktop: " + str(files_on_desktop_counter) + "\n")
file_out.close()
# this has to be done before the files are moved, or otherwise it will just print out one txt file
# if it already exists, then it won't be overwritten, or anything added to it
# it must be deleted each time the script is run if you want a fresh file instead of appended data

# move files into new folders if that suffix occurs more than 5 times
for i in dictionary:
    if dictionary[i] > 5:

        # makes the new folders, if the file with that suffix > 5 in frequency
        new_addition = i[1:] + "_files"
        new_folder_name = folder_directory / new_addition
        new_folder_name.mkdir(exist_ok=True)

        for file in folder_directory.iterdir():
            if file.suffix == i:
                new_file_path = new_folder_name / file.name
                file.rename(new_file_path)
