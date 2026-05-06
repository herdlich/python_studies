# File Sorter

This Python script sorts files from the `files` folder into categorized subfolders inside `sorted`.  
It supports Images, Documents, Archives, Audio, Videos, and moves all other files into `Other`.  
Duplicate filenames are handled by adding `_1`, `_2`, etc.

**Usage:**  
1. Put files in the `files` folder.  
2. Run: `python sort_files.py`  
3. Sorted files appear in `files/sorted/` by category.

**Requirements:** Python 3.x (standard libraries: `pathlib`, `shutil`)

**Notes:** Only top-level files are sorted; modify `extensions` to add or remove categories.