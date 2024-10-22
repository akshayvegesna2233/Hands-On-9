Dynamic Hash Table Implementation
This project implements a hash table that can grow and shrink as needed. It uses integer keys and values.
How it works:
Hash Function:
Uses both multiplication and division methods
Multiplies the key by the golden ratio
Takes the fractional part and multiplies it by the table size
Uses modulo to get the final index
Collision Handling:
Uses chaining with a doubly linked list
Each bucket in the table can hold multiple items
Data Structure:
Uses a list to represent the hash table
Each element in the list is the head of a chain
Key Operations:
Insert: Adds a new key-value pair
Remove: Deletes a key-value pair
Retrieve: Finds the value for a given key
Dynamic Resizing:
Doubles the size when the table is full
Halves the size when the table is one-fourth empty
Rehashes all items when resizing
Main Components:
DualNode: Represents an item in the hash table
DynamicHashStructure: The main hash table class
Usage:
Create a new hash table
Insert items using keys and values
Retrieve values using keys
Remove items using keys
This implementation provides efficient insertion, deletion, and retrieval of items while automatically managing the size of the hash table for optimal performance.