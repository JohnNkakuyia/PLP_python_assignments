# Assignment_Week_2_ 📃 List in python 

## 📘 Week Two Assignment Description

This assignment demonstrates basic list operations in Python. The tasks include:

- Creating an empty list called `my_list`
- Appending elements: `10`, `20`, `30`, `40`
- Inserting the value `15` at the second position
- Extending the list with `[50, 60, 70]`
- Removing the last element
- Sorting the list in ascending and descending order
- Reversing the list
- Finding and printing the index of the value `30`

## 🧠 Sample Code Used

```python
# Creating an empty list
my_list = []

# Appending elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting value at the second position
my_list.insert(1, 15)

# Extending the list
my_list.extend([50, 60, 70])

# Removing the last element
my_list.pop()

# Sorting in ascending order
my_list.sort()

# Sorting in descending order
my_list.sort(reverse=True)

# Reversing to ascending
my_list.reverse()

# Finding index of value 30
index_30 = my_list.index(30)
print(index_30)  # Output: 3

```
# Week_3_Assignment 📱Price and Discount calculator 

## Description
This Python program calculates the final price of an item after applying a discount.  
The discount is only applied if the discount percentage is **20% or higher**; otherwise, the original price is returned without any change.



## Features
- Function `calculate_discount(price, discount_percent)`:
  - Accepts the original price and discount percentage as parameters.
  - Checks if the discount is **≥ 20%**.
  - If yes, applies the discount and returns the final price.
  - If not, returns the original price unchanged.
- Prompts the user to:
  - Enter the original price of the item.
  - Enter the discount percentage.
- Displays the final price based on the discount condition.


# Week_4_ Assignment 📂 File Handling & Error Handling in Python  

## 📝 Project Overview  
This project demonstrates **file operations** and **exception handling** in Python.  
It covers:  
- Reading from and writing to text files.  
- Modifying content (uppercase conversion).  
- Handling errors such as missing files or permission issues.  
- Writing results into a new file.  

---

## 🚀 Features  
1. **File Read & Write Challenge 🖋️**  
   - Reads from `input.txt`.  
   - Converts text to **UPPERCASE**.  
   - Saves results into `output.txt`.  
   - Prints a success message ✅.  

2. **Error Handling Lab 🧪**  
   - Asks the user for a filename.  
   - Handles errors if the file:  
     - ❌ Doesn’t exist (`FileNotFoundError`).  
     - ⚠️ Can’t be accessed due to permissions (`PermissionError`).  
   - Reads and prints content if successful.  

---




