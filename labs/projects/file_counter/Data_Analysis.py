"""
    -> the file_counter.py file builds an sql file
    -> this contains information about the file types on the desktop, over time
    -> each time the script is run, information about the files on the desktop is appended to this sql file
    -> this Data_Analysis.py file will extract information about the sql database, and append it to the database
        -> this is similar to summary statistics
"""

#IMPORT MODULES
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import re #the regex module, for searching database elements
from collections import defaultdict

#PATH OF SQL FILE WE ARE WORKING WITH
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#the path of the sql file which we want to read from and append to
file_path = "/Users/francescapanteli/Desktop/CodingNomads-python-201/labs/projects/file_counter/after_module_07/Desktop file summary.sql"

#READ IN THE SQL FILE, AND STORE CONTENTS IN A VARIABLE
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# We first read the contents of the SQL file, and store them in the contents variable
with open(file_path, "r") as f: #this is a context manager; it is easier than three lines (including open() and close())
    contents = f.read()

#INITIALISE VARIABLES TO EXTRACT INFORMATION ABOUT THE DATABASE
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Split into blocks, each starting with "Desktop file summary:"
    #all of the contents of the sql file are now stored in the contents variable
blocks = contents.strip().split("Desktop file summary:")

#initialise variables
    #these variables contain the values of the element we want to extract
total_files = 0 #initialise the file counter at zero
file_type_counts = defaultdict(int) #the default value of the dictionary is zero (a number), which we wll populate
items_per_day = defaultdict(int)

#EXTRACT INFORMATION ABOUT THE DATABASE
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""
    -> the contents of the sql file has been read into the scipt and stored in the contents variable 
    -> this was then split into blocks, starting with "Desktop file summary"
        -> each of these blocks in the sql file corresponds to a time which the file_counter.py script was run
        -> both of these scripts are being used to write to this sql file 
    -> we then iterate through the blocks which have been extracted from the sql file 
    -> to build the values of the variables which we want to extract
        -> each time, we are iterating through the values in the blocks 
"""

#we are iterating through all of the blocks in the sql file
for block in blocks: #iterate through the different blocks in the sql file whihch we just stripped
    block = block.strip() #initialise block
    if not block: #carry on if we have a new line (if it's not a block)
        continue

"""
    -> example contents of the sql file, after the file_counter.py script has been run:
        Desktop file summary: {'.png': 31, '.jpeg': 8}
        Script run at: 2025-09-25 13:16:45
        Number of pngs on desktop: 31
        Number of folders on the desktop: 12
        -> we have hit a new file summary when the block contains {}
            -> we first search for this {} in the block being iterated through 
            -> this is done using the .search method in the re (regex) module we imported 
            -> file_summary_match returns a re.Match object if it finds a match, and if not then a None object
            -> this is important, because the sql file also contains information which the Data_Analysis.py file contributes to it (without the {}'s in this example) 
            -> we are grabbing all of the information between the {}'s (curly braces) for the block and storing it in the file_summary_match variable  
        -> file_summary contians the information between the {}'s in the file summary, and is done with the re (regex) module while iterating through this block in the sql file
            -> we then evaluate the file_summary_match None type object, or re.Match object
            -> file_summary_match should contain all of the information in between the {}'s in the block 
            -> if it is a None type object, then the file_summary variable is set to an empty dictionary (no files)
            -> eval means 'convert this to Python'
            -> we are taking all of the information in between the {}'s in the block and storing it in this variable 
            -> otherwise, we have an empty block 
"""

    # Extract file summary dictionary
    file_summary_match = re.search(r"(\{.*?\})", block) #search for the file summary in the block we are iterating through
        #the sql file contents were read in and split into blocks
        #we have hit a new file summary when the block contains {}
    file_summary = eval(file_summary_match.group(1)) if file_summary_match else {}

"""
    -> we now have file_summary 
        -> this is a dictionary that contains a file summary for this block 
        -> for example, "'.png': 31, '.jpeg': 8" 
        -> we are iterating through the suffix in the dictionary and the number it contains, for this block 
        -> and then, adding the count to the file_type_counts list which we previously initialised
        -> this is also added to the total files 
        -> this is done as a list, containing the dfferent file suffixes which were found on the desktop 
"""

    # Count files by type
    for ext, count in file_summary.items():
        file_type_counts[ext] += count
        total_files += count

"""
    -> we then want to extract the total number of files by date 
    -> this entire method 
        -> takes the sql file, reads it in and stores its contents in a contents variable 
        -> breaks the contents down into blocks
        -> iterates through each block
        -> extracts the information we want (contained in a summary dictionary)
        -> forms counters for these elements 
        -> appends the information back to the sql file and prints it out to the user
    -> date_match 
        -> we are using the re (regex) module again to search for the timestap stored in the block   
        -> this timestamp is of a particular format 
        -> this object is a None type, if there is no timestamp, or an re.Match object
    -> num_fodlders_match 
        -> we search the block using the same method as before for the number of folders which are on the desktop 
        -> this is again stored as a None type object, or as an re.Match object 
"""

    # Count total items on that date (files + folders)
    date_match = re.search(r"Script run at:\s*(\d{4}-\d{2}-\d{2})", block)
    num_folders_match = re.search(r"Number of folders on the desktop:\s*(\d+)", block)

"""
    -> if block 
        -> if there is a timestamp in the block 
        -> we extract information about the date, and the amount of desktop files cleaned on given dates
        -> to estract the date, we extract the first element in the date_match variable 
            -> this is stored in the date variable 
        -> the same method is then used to extract the number of folders on the desktop
            -> this is stored in the num_folders variable 
            -> if there are no folders on the desktop, then this variable is set to zero
        -> the number of files in the block 
            -> this is stored in the num+file_in_block variable 
            -> we are adding all of the values in the file_summary variable
            -> these values contain the number of files of different types
        -> for the items per day, on a particular date
            -> this is stored in the items_per_day variable 
            -> we append this to the elements from the previous blocks, where the file_counter.py script was run on the same day
            -> the dat variable is the day in the timestamp for the current sql block being terated thorugh 
            -> the items per day, on this date, is the number of files in the block plus the number of folders
"""

    if date_match:
        date = date_match.group(1)
        num_folders = int(num_folders_match.group(1)) if num_folders_match else 0
        num_files_in_block = sum(file_summary.values())
        items_per_day[date] += num_files_in_block + num_folders

#PRINT DATABASE INFORMATION
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""
    Finding the day with the most items 
    -> we have built out an items_per_day dictionary, which contains the number of items which were cleaned per day by the file_counter.py file 
        -> we want to extract the day with the maxiumum value that this contains (most_tems_day)
        -> and then to extract the number of items which were cleaned in this day on the desktop 
            -> this is stored in the most_items_count variable  
"""

# Find the day with the most items
most_items_day = max(items_per_day, key=items_per_day.get)
most_items_count = items_per_day[most_items_day]

"""
    Finding the most common file type in the database 
    -> file_type_counts contains the amount of different types of files that were found in the database, and their different amounts
    -> we first extract the day that contains the most common file type, and store it in the most_common_file_type variable
    -> the total number of files of this type are then stored in the most_common_file_count variable 
"""

# Find the most common file type in the database
most_common_file_type = max(file_type_counts, key=file_type_counts.get)
most_common_file_count = file_type_counts[most_common_file_type]

"""
    Appending the information to the Desktop file summary.sql database
    -> we then define an f string literal, which contains the information we want to append to the database
    -> this is contained in a doc-string like object; it is an f string that spans multiple lines 
    -> a context manager is then used to append this information to the database
        -> the first argument of this is the path of the sql database
        -> the second argument is append mode (we want to add to the end of the file, not write over it)
        -> if write mode is used, then this will wipe all of the information that the sql file contains
    -> the information is finally printed to the console when the script is run
        -> this allows the user to see what the script is adding to the sql file (the same thing is printed in the terminal) 
"""
# Prepare summary string to append
summary_to_append = f"""
Desktop Analysis Summary:
Total files ever on desktop: {total_files}
Total number for each file type: {dict(file_type_counts)}
Day with most items: {most_items_day} ({most_items_count} items)
Most common file type: {most_common_file_type} ({most_common_file_count} files)
Script run at: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

# Append the summary to the SQL file
with open(file_path, "a") as f:
    f.write(summary_to_append)

# Print to console
print(summary_to_append)
