Solution to JJB's web server circus.
===================
  
#Instructions

Step 1:  Using a Mac save delete_crap.py to your uploads directory


Step 2:  Create a keep_list.csv file like the one in this repository.  
The keep_list.csv file contains a list of files you want to keep.  
Make sure to add the delete_crap.py and keep_list.csv
to your CSV list, otherwise the app will try and delete those files which would be bad.
Save the keep_list.csv file to the same directory where delete_crap.py lives.


Step 3:  Open the terminal and CD to the uploads directory


Step 4:  Run this command below in the terminal


```
python delete_crap.py keep_list.csv /Users/doug5997/Pictures/uploads
```

Note:  The above python command takes two parameters:
1) path to list containing the files your want to keep
2) path to the top directory you are trying to clean
