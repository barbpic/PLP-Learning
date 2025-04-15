```markdown
# Python Data Structures and Strings

## Day 1: Introduction to Data Structures

So far, you have only stored small bits of data in a variable. This was either an integer, Boolean, or a string.  

But what happens if you need to work with more complex information, such as a collection of data like a list of people or a list of companies? Data structures are designed for this very purpose.  
![Data Structures](images/image-1.png)

A data structure allows you to organize and arrange your data to perform operations on them. Python has the following built-in data structures: **List**, **Dictionary**, **Tuple**, and **Set**. These are all considered non-primitive data structures, meaning they are classed as objects.  

Along with the built-in data structures, Python allows users to create their own, such as **Stacks**, **Queues**, and **Trees**. Each data structure can be designed to solve a particular problem or optimize a current solution to make it more performant.

### Mutability and Immutability

- **Mutable**: Data inside the structure can be modified (e.g., List).
- **Immutable**: Data cannot be modified once set (e.g., Tuple).

---

## Day 2: Python Lists

### Creating a Python List

A list is created in Python by placing items inside `[]`, separated by commas. For example:  
![Creating a List](images/image-18.png)

A list can have any number of items and they may be of different types (integer, float, string, etc.).  
![List Example](images/image-17.png)

### Accessing List Elements

Each item in a list is associated with an index number starting from `0`.  
![Accessing List Elements](images/image-16.png)

### Slicing a List

You can access a section of items using the slicing operator `:`.  
![Slicing Example](images/image-15.png)

### Adding Elements to a List

1. **Using `append()`**: Adds an item at the end of the list.  
2. **Using `extend()`**: Adds all items of one list to another.  
![Adding Elements](images/image-13.png)

### Changing List Items

Lists are mutable, so you can change items by assigning new values.  
![Changing List Items](images/image-14.png)

### Removing Items from a List

1. **Using `del`**: Removes one or more items.  
2. **Using `remove()`**: Deletes a specific item.  
![Removing Items](images/image-11.png)

### Python List Methods

Python provides many useful methods for lists.  
![List Methods](images/image-9.png)

### Iterating Through a List

You can use a `for` loop to iterate over list elements.  
![Iterating Example](images/image-10.png)

### List Comprehension

A concise way to create lists.  
![List Comprehension](images/image-6.png)

---

## Day 3: Python Tuples

A tuple is similar to a list, but it is **immutable**.  

### Creating a Tuple

Tuples are created using `()`.  
![Creating a Tuple](images/image-4.png)

### Accessing Tuple Elements

1. **Indexing**: Access elements using their index.  
2. **Negative Indexing**: Access elements from the end.  
![Accessing Tuples](images/image-5.png)

### Tuple Methods

Tuples have limited methods since they are immutable.  
![Tuple Methods](images/image-3.png)

---

## Day 4: Python Sets

A set is a collection of **unique** data.  

### Creating a Set

Sets are created using `{}` or the `set()` function.  
![Creating a Set](images/image-35.png)

### Adding and Updating Set Items

- **`add()`**: Adds a single item.  
- **`update()`**: Adds multiple items from other collections.  
![Adding Items](images/image-31.png)

### Removing Set Items

- **`discard()`**: Removes a specified item.  
![Removing Items](images/image-34.png)

### Set Operations

1. **Union (`|`)**: Combines all elements from two sets.  
2. **Intersection (`&`)**: Finds common elements.  
3. **Difference (`-`)**: Finds elements in one set but not the other.  
4. **Symmetric Difference (`^`)**: Finds elements in either set but not both.  
![Set Operations](images/image-26.png)

---

## Day 5: Python Strings

A string is a sequence of characters enclosed in single or double quotes.  

### Accessing String Characters

1. **Indexing**: Access characters using their index.  
2. **Negative Indexing**: Access characters from the end.  
3. **Slicing**: Access a range of characters.  
![Accessing Strings](images/image-47.png)

### String Operations

- **Concatenation**: Use `+` to join strings.  
- **Membership Test**: Use `in` to check if a substring exists.  
![String Operations](images/image-42.png)

### String Methods

Python provides various methods to manipulate strings.  
![String Methods](images/image-43.png)

### Escape Sequences

Use `\` to include special characters in strings.  
![Escape Sequences](images/image-39.png)

### String Formatting

Use **f-strings** for easy string formatting.  
![String Formatting](images/image-41.png)

---

## Additional Resources

- [Python Lists and Tuples](https://www.knowledgehut.com/tutorials/python-tutorial/python-lists-tuples)
- [Python Dictionaries](https://realpython.com/python-dicts/)
- [Python Sets](https://realpython.com/python-sets/)
- [Python Strings](https://www.geeksforgeeks.org/python-string/)
```
