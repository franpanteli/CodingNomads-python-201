# Add the code for the file counter script that you wrote in the course.
# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
from pprint import pprint #to pretty print (pprint) the dictionary
import pathlib
from pathlib import Path

# The path where we want to create the new folder
folder_directory = pathlib.Path('/Users/francescapanteli/Desktop')
    #this is an absolute path, which means the script can be run from anywhere


files_on_desktop = []
files_on_desktop_counter = 0
png_counter = 0

for file in folder_directory.iterdir():
    if len(file.suffix) > 0: #some of the file suffixes are '', with lengths of 0
        files_on_desktop.append(file.suffix)
    if file.suffix == '.png':
        png_counter += 1 #count the number of png files on the desktop
    else:
        files_on_desktop_counter += 1 #counts the number of folders on the desktop

keys = list(set(files_on_desktop))
values = [files_on_desktop.count(i) for i in keys]

dictionary = dict(zip(keys,values))
print("Desktop file summary: ", dictionary)

#write the desktop data to a file
file_out = open("Desktop file summary.csv","a") #"w" has to be in quotation marks
    #this was changed to a csv file, rather than a txt file, during the third module exercises of the course
    #change this to append because we are counting how the number of files on the desktop changes over time
file_out.write("Desktop file summary: "+str(dictionary))
file_out.write("\n")
file_out.write("Number of pngs on desktop: "+str(png_counter))
file_out.write("\n")
file_out.write("Number of folders on the desktop: "+ str(files_on_desktop_counter))
file_out.close()
    #this has to be done before the files are moved, or otherwise it will just print out one txt file
    #if it already exists, then it won't be overwritten, or anything added to it
    #it must be deleted each time the script is run

for i in dictionary:
    if dictionary[i]>5:

        #makes the new folders, if the file with that suffix > 5 in frequency
        new_addition = i[1:]+"_files"
        new_folder_name = folder_directory / new_addition
        new_folder_name.mkdir(exist_ok=True)

        for file in folder_directory.iterdir():
            if file.suffix == i:
                new_file_path = new_folder_name / file.name
                file.rename(new_file_path)