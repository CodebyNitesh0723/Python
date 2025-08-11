# 🧠 Chapter 6: Lists — Summary Guide

# 📦 What Is a List?
# A list is a collection of items (strings, numbers, other lists, etc.) stored in one variable.
# Example:
# spam = ['cat', 'bat', 'rat', 'elephant']

# 🧩 Nested Lists
# Lists can contain other lists.
# Example:
# spam = [['cat', 'bat'], [10, 20]]
# print(spam[0][1])  # 'bat'

# 🔁 Negative Indexing
# -1 = last item
# -2 = second last item
# Example:
# spam[-1]  # 'elephant'

# ✂️ Slicing Lists
# Use : to get multiple items.
# Example:
# spam[1:3]  # ['bat', 'rat']
# spam[:2]   # ['cat', 'bat']
# spam[1:]   # ['bat', 'rat', 'elephant']

# 📏 len() Function
# Gives the number of items in the list.
# Example:
# len(spam)

# 🔄 Modifying Lists
# Replace a value in a list using its index.
# Example:
# spam[1] = 'aardvark'  # Replace 'bat' with 'aardvark'

# ➕ Concatenation and ✖️ Replication
# Example:
# [1, 2] + ['A', 'B']  # [1, 2, 'A', 'B']
# ['X'] * 3            # ['X', 'X', 'X']

# ❌ Deleting Values with del
# Example:
# del spam[2]  # Deletes the item at index 2


# Lists — Quick Cheat Sheet
# A list is a collection of items stored in one variable → spam = ['cat', 'bat', 'rat', 'elephant']
# Lists can contain other lists (nested lists) → spam = [['cat', 'bat'], [10, 20]]
# Access nested list items → spam[0][1]  # 'bat'
# Negative indexing: -1 = last item, -2 = second last → spam[-1]  # 'elephant'
# Slicing: spam[1:3] → ['bat', 'rat'], spam[:2] → ['cat', 'bat'], spam[1:] → ['bat', 'rat', 'elephant']
# len(list) gives number of items → len(spam)
# Replace list items → spam[1] = 'aardvark'
# Concatenate lists → [1, 2] + ['A', 'B'] → [1, 2, 'A', 'B']
# Replicate lists → ['X'] * 3 → ['X', 'X', 'X']
# Delete items → del spam[2]
