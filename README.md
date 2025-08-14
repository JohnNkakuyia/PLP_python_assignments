# Assignment_Week2

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

```python
# Week 3 Assignment

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


## Usage
1. Run the program in a Python environment (e.g., VS Code, PyCharm, Jupyter Notebook, or terminal).
2. Input the **original price** when prompted.
3. Input the **discount percentage**.
4. View the final price after applying the discount rule.

---

