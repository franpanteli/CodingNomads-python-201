# Data_Analysis.py

import re
from collections import defaultdict

file_path = "/Users/francescapanteli/Desktop/CodingNomads-python-201/labs/projects/file_counter/after_module_07/Desktop file summary.sql"

# Read the contents of the SQL file
with open(file_path, "r") as f:
    contents = f.read()

# Split into blocks, each starting with "Desktop file summary:"
blocks = contents.strip().split("Desktop file summary:")

total_files = 0
file_type_counts = defaultdict(int)
items_per_day = defaultdict(int)

for block in blocks:
    block = block.strip()
    if not block:
        continue

    # Extract file summary dictionary
    file_summary_match = re.search(r"(\{.*?\})", block)
    file_summary = eval(file_summary_match.group(1)) if file_summary_match else {}

    # Count files by type
    for ext, count in file_summary.items():
        file_type_counts[ext] += count
        total_files += count

    # Count total items on that date (files + folders)
    date_match = re.search(r"Script run at:\s*(\d{4}-\d{2}-\d{2})", block)
    num_folders_match = re.search(r"Number of folders on the desktop:\s*(\d+)", block)
    if date_match:
        date = date_match.group(1)
        num_folders = int(num_folders_match.group(1)) if num_folders_match else 0
        num_files_in_block = sum(file_summary.values())
        items_per_day[date] += num_files_in_block + num_folders

# Find the day with the most items
most_items_day = max(items_per_day, key=items_per_day.get)
most_items_count = items_per_day[most_items_day]

# Find the most common file type ever
most_common_file_type = max(file_type_counts, key=file_type_counts.get)
most_common_file_count = file_type_counts[most_common_file_type]

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
