import math

class DualNode:
    def __init__(self, identifier, content):
        self.identifier = identifier
        self.content = content
        self.next_node = None
        self.prev_node = None

class DynamicHashStructure:
    def __init__(self, initial_size=8):
        self.container_size = initial_size
        self.item_count = 0
        self.containers = [None] * self.container_size

    def calculate_index(self, identifier):
        # Combining multiplication and division methods
        phi = (1 + math.sqrt(5)) / 2  # Golden ratio
        temp = identifier * phi
        fractional = temp - int(temp)
        multiplied = int(self.container_size * fractional)
        return multiplied % self.container_size

    def restructure(self, new_size):
        new_containers = [None] * new_size
        for container in self.containers:
            current = container
            while current:
                subsequent = current.next_node
                new_idx = self.calculate_index(current.identifier)
                current.next_node = new_containers[new_idx]
                current.prev_node = None
                if new_containers[new_idx]:
                    new_containers[new_idx].prev_node = current
                new_containers[new_idx] = current
                current = subsequent
        self.containers = new_containers
        self.container_size = new_size

    def insert_item(self, identifier, content):
        if self.item_count >= self.container_size:
            self.restructure(self.container_size * 2)

        idx = self.calculate_index(identifier)
        fresh_node = DualNode(identifier, content)
        fresh_node.next_node = self.containers[idx]
        if self.containers[idx]:
            self.containers[idx].prev_node = fresh_node
        self.containers[idx] = fresh_node
        self.item_count += 1

    def remove_item(self, identifier):
        idx = self.calculate_index(identifier)
        current = self.containers[idx]
        while current:
            if current.identifier == identifier:
                if current.prev_node:
                    current.prev_node.next_node = current.next_node
                else:
                    self.containers[idx] = current.next_node
                if current.next_node:
                    current.next_node.prev_node = current.prev_node
                self.item_count -= 1

                if self.item_count <= self.container_size // 4 and self.container_size > 8:
                    self.restructure(self.container_size // 2)
                return
            current = current.next_node

    def retrieve_item(self, identifier):
        idx = self.calculate_index(identifier)
        current = self.containers[idx]
        while current:
            if current.identifier == identifier:
                return current.content
            current = current.next_node
        return None  # Identifier not found

    def get_item_count(self):
        return self.item_count

    def get_container_size(self):
        return self.container_size

# Test the DynamicHashStructure
if __name__ == "__main__":
    hash_structure = DynamicHashStructure()

    # Insert some identifier-content pairs
    hash_structure.insert_item(7, 70)
    hash_structure.insert_item(17, 170)
    hash_structure.insert_item(27, 270)

    # Retrieve and print contents
    print(f"Content for identifier 7: {hash_structure.retrieve_item(7)}")
    print(f"Content for identifier 17: {hash_structure.retrieve_item(17)}")
    print(f"Content for identifier 27: {hash_structure.retrieve_item(27)}")

    # Remove an identifier
    hash_structure.remove_item(17)

    # Try to retrieve the removed identifier
    print(f"Content for identifier 17 after removal: {hash_structure.retrieve_item(17)}")

    # Insert many items to test resizing
    for i in range(100):
        hash_structure.insert_item(i, i * 10)

    print(f"Final item count: {hash_structure.get_item_count()}")
    print(f"Final container size: {hash_structure.get_container_size()}")

#Output
Content for identifier 7: 70
Content for identifier 17: 170
Content for identifier 27: 270
Content for identifier 17 after removal: None
Final item count: 102
Final container size: 128