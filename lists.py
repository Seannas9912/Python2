#Lesson 1: Lists
# A list is a collection of items that can be of different types.
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

fruits[1] = "orange"  # Change the value of the second item
print(fruits)  # Output: ['apple', 'orange', 'cherry']

# Adding an item to the list
fruits.append("kiwi")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'kiwi']