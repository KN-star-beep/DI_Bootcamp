import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        # Step 2: Initialize attributes
        self.items = items if items is not None else []
        self.page_size = int(page_size)
        self.current_idx = 0
        
        # Calculate total pages: total items divided by size, rounded up
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 1

    # Step 3: Implement slicing logic
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # Step 4: Navigation Methods
    def go_to_page(self, page_num):
        # Convert to 0-based index for internal logic
        target = int(page_num) - 1
        if target < 0 or target >= self.total_pages:
            raise ValueError(f"Page {page_num} is out of range. Total pages: {self.total_pages}")
        
        self.current_idx = target
        return self # Allows chaining

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # Step 5: Bonus __str__ method
    def __str__(self):
        visible = self.get_visible_items()
        return "\n".join(visible)

# Step 6: Test Your Code
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(f"Page 1: {p.get_visible_items()}") # ['a', 'b', 'c', 'd']

p.next_page()
print(f"Page 2: {p.get_visible_items()}") # ['e', 'f', 'g', 'h']

p.last_page()
print(f"Last Page: {p.get_visible_items()}") # ['y', 'z']

# Testing Method Chaining Bonus
# Moves 3 pages forward from page 1 (to page 4)
print(f"Chained result: {p.first_page().next_page().next_page().next_page().get_visible_items()}") 
# Output: ['m', 'n', 'o', 'p']