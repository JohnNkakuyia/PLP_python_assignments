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
