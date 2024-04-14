# IP Address Allow List Program (Python) 

## Objective

The objective of this IP Allow List program is to automate the management of IP addresses permitted to access restricted content. This automation streamlines the process of managing access control measures based on IP addresses, reducing the likelihood of unauthorised access and enhancing overall security.

### Skills Learned

- **File Handling**: Ability to read and write text files in Python, crucial for accessing and updating lists of IP addresses.
- **Data Manipulation**:  Understanding how to convert strings into lists and vice versa, facilitating the processing of data within the program.
- **Iterating through Lists**: Proficiency in using loops to iterate through lists of IP addresses and perform actions based on specific criteria.
- **Conditional Statements**: Capability to implement conditional statements to check for certain conditions, such as the presence of IP addresses in the allow list.
- **String Manipulation**: Basic string manipulation skills to format and update text data as needed.

### Tools Used

- Visual Studio Code (VS Code)
- Python Programming Language

## Steps
### 1. Ensuring that the Python and text files _allow_list.txt_ and _remove_list.txt_ are stored in the same directory.
Create two text files named "allow_list.txt" and "remove_list.txt" in the same directory as your Python file. Populate these files with lists of IP addresses, with each IP address on a separate line.
You can also use the files I have provided for simplicity. 

![image](https://github.com/Ammarisanewbie/IP-AllowList/assets/108499824/b0c60443-5326-45f8-80ac-bb017b049bd5)

*Ref 1: Files in the same Directory*

### 2. Open the Input Files
Start by opening two input files using the open() function in Python: "_allow_list.txt_" and "_remove_list.txt_". 
These files contain lists of IP addresses, with "allow_list.txt" containing the initial list of IP addresses permitted to access and "remove_list.txt" containing the list of IP addresses to be removed from the allow list
This works for files in _.txt_ and _.csv_ format

![image](https://github.com/Ammarisanewbie/IP-AllowList/assets/108499824/c9c91a7c-4c62-41df-8cc7-d2e1bbaa824b)

*Ref 2: How to Open text files*

- `with open()` is used to open the input text files. These files contain the list of IP addresses, with "allow_list.txt" containing the initial list of IP addresses permitted to access and "remove_list.txt" containing the list of IP addresses to be removed from the allow list.
- `r`: the `r` parameter is passed to inform Python that we will read the file input.  _Some other parameters include:_
  -  _w : write_
  -   _a : append_
- `file`: is a self-declared local variable of your choice.
- *Important: Only the file's directory, "r" and `file` are mutable.


### 3. Read Files Content

![image](https://github.com/Ammarisanewbie/IP-AllowList/assets/108499824/05fe3ad7-9f9d-423d-ba70-edc899d66012)

*Ref 3: How to Read Files Content*

- Using `read()` method, the code reads the content of the input files and stores them as strings in _allowIP_ and _removeIP_
- Initialising them in variables allows us to use the contents outside the block.

### 4. Convert Strings to Lists

![image](https://github.com/Ammarisanewbie/IP-AllowList/assets/108499824/bdfb55ec-7d39-48c7-b3dd-5d67c0952367)

*Ref 4: How to Convert Strings to Lists*

- Using `split()` method, the strings stored in _allowIP_ and _removeIP_ are then converted into lists of IP addresses.
- This method splits the string into substrings based on whitespace (_by default, leaving it empty_) and returns a list of these substrings.
- `split(x)`: _x_ is the parameter defined based on where you wish to split. _Some other parameters include:_
  - _, :  split at commas_
  - _\n : split at newlines _
- `split()` method is typically used to filter out unwanted content from what you need

### 5. Iterate Through the Remove List 

![image](https://github.com/Ammarisanewbie/IP-AllowList/assets/108499824/1bcecb49-a3b6-4e6a-9dab-0b19c6d040da)

*Ref 5: Iterating through remove_list*

- The code iterates through each IP address in the remove list using a `for` loop.
- For each IP address (ip) in the remove list, it checks if the IP address is present in the allow list (allow_list).
  
### 6. Remove Matching IP Addresses 

![image](https://github.com/Ammarisanewbie/IP-AllowList/assets/108499824/ac87c1a2-390c-4e43-86b3-b115945d3a1c)

*Ref 6: Removing IP*

- Using IFELSE, f an IP address(ip) from the remove list is found in the allow list
- it is removed using the `remove()` list method.
- This ensures that any IP addresses specified for removal are excluded from the final allow list

### 7. Update the Allow List File
  
![image](https://github.com/Ammarisanewbie/IP-AllowList/assets/108499824/8fb55eb7-14c1-4ae0-888b-a913553683da)

*Ref 7: Update new list of IP addresses into string*

- Initialising a new variable called `updated_allow_list`, we use `.join()` to join the remaining IP addresses in the allow list with newline characters `"\n"`
- This formatted string is then written back to the "allow_list.txt" file using the `write()` method.
- The code execution completes, and the allow list file is updated with the revised list of IP addresses.


